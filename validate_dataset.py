"""Audit labels.csv against the saved Internet responses, without training."""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    with (ROOT / 'labels.csv').open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        assert reader.fieldnames == ['text', 'label', 'note'], reader.fieldnames
        rows = list(reader)
    sources = json.loads((ROOT / 'data/source_posts.json').read_text(encoding='utf-8'))
    assert len(rows) == len(sources) >= 200
    originals = {}
    for path in (ROOT / 'data/collection').glob('page_*.json'):
        for post in json.loads(path.read_text(encoding='utf-8'))['data']:
            originals[post['id']] = post
    seen_ids, seen_text, seen_normalized, seen_bodies = set(), set(), set(), set()
    counts, authors = Counter(), Counter()
    for number, (row, source) in enumerate(zip(rows, sources), 1):
        original = originals[source['id']]
        assert number == source['row']
        assert original['subreddit'].lower() == 'asoiaf'
        assert original.get('is_self')
        assert not original.get('removed_by_category')
        assert original['author'].lower() not in ('automoderator', '[deleted]')
        assert original['selftext'].strip() not in ('[removed]', '[deleted]')
        expected = original['title'] + ('\n\n' + original['selftext'] if original['selftext'] else '')
        assert row['text'] == expected, f'Altered/truncated source at row {number}'
        assert row['text'].strip() and '\ufffd' not in row['text']
        assert source['title'] == original['title'] and source['body'] == original['selftext']
        assert hashlib.sha256(row['text'].encode('utf-8')).hexdigest() == source['text_sha256']
        assert source['url'] == 'https://www.reddit.com' + original['permalink']
        snapshot = ROOT / source['snapshot_file']
        assert hashlib.sha256(snapshot.read_bytes()).hexdigest() == source['snapshot_sha256']
        assert row['label'] in {'analysis', 'opinion', 'question'}
        assert row['label'] == source['label']
        assert row['note'] == source['note']
        assert 'pre-labeled by AI' in row['note'] and 'human review pending' in row['note']
        assert source['url'] in row['note']
        assert not re.search(r'\bcold\b', row['note'], re.I), 'Unexpected cold-label claim'
        assert source['id'] not in seen_ids
        assert row['text'] not in seen_text
        normalized = re.sub(r'\s+', ' ', row['text']).strip().casefold()
        assert normalized not in seen_normalized
        if original['selftext'].strip():
            body = re.sub(r'\s+', ' ', original['selftext']).strip().casefold()
            assert body not in seen_bodies, f'Repeated body at row {number}'
            seen_bodies.add(body)
        seen_ids.add(source['id'])
        seen_text.add(row['text'])
        seen_normalized.add(normalized)
        counts[row['label']] += 1
        authors[original['author']] += 1
    assert set(counts) == {'analysis', 'opinion', 'question'}
    assert max(counts.values()) / len(rows) <= .50
    assert max(authors.values()) <= 5
    print(f'PASS: {len(rows)} rows, exact text matches to {len(seen_ids)} Internet source records.')
    print('PASS: exact text/body/normalized duplicates absent; notes and provenance complete.')
    print(f'Labels: {dict(counts)}; largest share: {max(counts.values()) / len(rows):.1%}.')
    print(f'Authors: {len(authors)}; maximum posts per author: {max(authors.values())}.')
    print('Status: 200 AI pre-labels, 0 cold labels, human review pending; no training performed.')


if __name__ == '__main__':
    main()
