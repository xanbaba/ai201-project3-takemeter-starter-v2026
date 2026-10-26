"""Collect archived public r/asoiaf submissions; never generate post text.

Run from the repository root. API snapshots retain the original text strings.
This script does not assign labels or perform train/test splitting.
"""
import hashlib
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'data' / 'collection'
ENDPOINT = 'https://arctic-shift.photon-reddit.com/api/posts/search'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = []
    before = None
    all_posts = {}
    for page in range(1, 9):
        params = {'subreddit': 'asoiaf', 'limit': 100}
        if before is not None:
            params['before'] = before
        url = ENDPOINT + '?' + urllib.parse.urlencode(params)
        path = OUT / f'page_{page:02d}.json'
        if path.exists():
            raw = path.read_bytes()
        else:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=40) as response:
                raw = response.read()
            path.write_bytes(raw)
        data = json.loads(raw)['data']
        manifest.append({'file': path.name, 'url': url,
                         'downloaded_utc': datetime.now(timezone.utc).isoformat(),
                         'sha256': hashlib.sha256(raw).hexdigest(), 'records': len(data)})
        for post in data:
            all_posts[post['id']] = post
        print(f'Page {page}: {len(data)} records; {len(all_posts)} unique', flush=True)
        if not data:
            break
        before = min(post['created_utc'] for post in data)
        time.sleep(1)
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    posts = sorted(all_posts.values(), key=lambda p: (-p['created_utc'], p['id']))
    candidates, excluded, seen = [], [], set()
    for post in posts:
        title, body = post.get('title', ''), post.get('selftext', '')
        text = title + ('\n\n' + body if body else '')
        reason = None
        if post.get('subreddit', '').lower() != 'asoiaf':
            reason = 'wrong_community'
        elif post.get('author', '').lower() in ('automoderator', '[deleted]'):
            reason = 'bot_or_deleted_author'
        elif post.get('removed_by_category') or body.strip() in ('[removed]', '[deleted]'):
            reason = 'removed_or_deleted'
        elif not post.get('is_self'):
            reason = 'non_self_submission'
        elif '\ufffd' in text:
            reason = 'replacement_character_in_archive'
        elif not title.strip():
            reason = 'empty_title'
        elif len(text) > 1200:
            reason = 'outside_short_submission_sampling_frame'
        elif text.strip().casefold() in seen:
            reason = 'duplicate_text'
        if reason:
            excluded.append({'id': post['id'], 'reason': reason})
        else:
            seen.add(text.strip().casefold())
            candidates.append({'id': post['id'], 'title': title, 'body': body,
                               'text': text, 'url': 'https://www.reddit.com' + post['permalink'],
                               'created_utc': post['created_utc']})
    for name, data in [('candidates.json', candidates), ('exclusions.json', excluded)]:
        (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Eligible short submissions: {len(candidates)}; excluded: {len(excluded)}')


if __name__ == '__main__':
    main()
