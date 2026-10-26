"""Prepare source-backed dataset rows from the recorded, individually assigned labels.

Does not generate post text, infer labels, or split data. build_labels.mjs writes
the final CSV; validate_dataset.py independently checks it against API snapshots.
"""
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data' / 'collection'


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def main():
    candidates = read_json(DATA / 'candidates.json')
    annotations = read_json(DATA / 'annotations.json')
    manifest = read_json(DATA / 'manifest.json')
    originals = {}
    for page in manifest:
        path = DATA / page['file']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == page['sha256']
        for post in read_json(path)['data']:
            originals[post['id']] = (post, page)
    authors, selection_exclusions = Counter(), []
    selected = []
    for item in candidates:
        post_id = item['id']
        if post_id not in annotations:
            selection_exclusions.append({'id': post_id, 'reason': 'not_annotated'})
            continue
        label, rationale = annotations[post_id]
        if label == 'exclude':
            selection_exclusions.append({'id': post_id, 'reason': rationale})
            continue
        original, page = originals[post_id]
        if authors[original['author']] >= 5:
            selection_exclusions.append({'id': post_id, 'reason': 'author_cap_5'})
            continue
        if len(selected) >= 200:
            selection_exclusions.append({'id': post_id, 'reason': 'after_200_eligible_rows'})
            continue
        expected = original['title'] + ('\n\n' + original['selftext'] if original['selftext'] else '')
        assert item['text'] == expected
        note = (f'pre-labeled by AI; human review pending; id={post_id}; '
                f'source={item["url"]}; rationale={rationale}')
        selected.append({
            'row': len(selected) + 1,
            'id': post_id,
            'url': item['url'],
            'author': original['author'],
            'subreddit': original['subreddit'],
            'created_utc': original['created_utc'],
            'title': original['title'],
            'body': original['selftext'],
            'text_sha256': hashlib.sha256(expected.encode('utf-8')).hexdigest(),
            'snapshot_file': 'data/collection/' + page['file'],
            'snapshot_sha256': page['sha256'],
            'archive_query': page['url'],
            'snapshot_recorded_utc': page['downloaded_utc'],
            'label': label,
            'note': note,
        })
        authors[original['author']] += 1
    assert len(selected) == 200
    counts = Counter(p['label'] for p in selected)
    assert max(counts.values()) / len(selected) <= .50
    source_path = ROOT / 'data' / 'source_posts.json'
    source_path.write_text(json.dumps(selected, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (DATA / 'selection_exclusions.json').write_text(
        json.dumps(selection_exclusions, indent=2) + '\n', encoding='utf-8')
    stats = {
        'rows': len(selected), 'label_counts': dict(counts),
        'label_shares': {k: v / len(selected) for k, v in counts.items()},
        'unique_authors': len(authors), 'max_posts_per_author': max(authors.values()),
        'title_only_rows': sum(not p['body'] for p in selected),
        'min_characters': min(len(p['title'] + ('\n\n' + p['body'] if p['body'] else '')) for p in selected),
        'max_characters': max(len(p['title'] + ('\n\n' + p['body'] if p['body'] else '')) for p in selected),
        'first_post_utc': datetime.fromtimestamp(min(p['created_utc'] for p in selected), timezone.utc).isoformat(),
        'last_post_utc': datetime.fromtimestamp(max(p['created_utc'] for p in selected), timezone.utc).isoformat(),
        'collected_unique': len(originals), 'short_candidates': len(candidates),
        'annotated_candidates': len(annotations),
        'initial_exclusions': dict(Counter(p['reason'] for p in read_json(DATA / 'exclusions.json'))),
        'cold_labels': 0, 'ai_prelabels': len(selected), 'human_reviews_completed': 0,
        'split_performed': False,
    }
    (DATA / 'dataset_summary.json').write_text(json.dumps(stats, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(stats, indent=2))


if __name__ == '__main__':
    main()
