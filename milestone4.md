# Milestone 4: Collection and labeling record

Collected October 26, 2026. Community: public r/asoiaf submissions.

## Delivered data

`labels.csv` contains 200 examples in the required `text,label,note` format,
with no train/validation/test split. Counts are analysis 83 (41.5%), opinion 54
(27.0%), and question 63 (31.5%). These are AI pre-labels awaiting human review.

The original posts were retrieved from the Internet. None of their text was
invented, paraphrased, translated, or completed by the assistant. Some authors
themselves discuss imagined scenes or AI tools; those are real public posts,
not synthetic examples added for this assignment.

## Collection method

Direct Python requests to Reddit returned HTTP 403. Collection therefore used
[Arctic Shift](https://github.com/ArthurHeitmann/arctic_shift), a public Reddit
archive, through its [documented post-search API](https://github.com/ArthurHeitmann/arctic_shift/blob/master/api/README.md).

1. Retrieve eight chronological pages of 100 r/asoiaf submissions each using
   `/api/posts/search?subreddit=asoiaf&limit=100` and a `before` timestamp for
   subsequent pages. No accounts, private groups, or invited content were used.
2. Save API response snapshots under `data/collection/page_*.json` and query
   URLs plus SHA-256 hashes in `manifest.json`. The first response was parsed
   and pretty-printed as JSON before saving; its original text strings are
   preserved. The remaining snapshots retain downloaded response bytes.
3. Filter known AutoModerator/deleted authors, removed/deleted records,
   non-self submissions, invalid replacement characters, empty titles, exact
   duplicate text, and submissions longer than 1,200 characters including the
   title. The first-pass exclusion counts are 202 removed/deleted, 109 non-self,
   15 bot/deleted-author, and 157 outside the short-post sampling frame.
4. Read complete retrieved text for the first 285 of 317 remaining candidates.
   Record each label and its reason, or a specific exclusion, in
   `data/collection/annotations.json`. Exclude repeated drafts, an announcement
   without a discussion position/request, a non-English submission, and a post
   with a substantial third-party song lyric. No source was shortened to make
   it eligible.
5. Limit selection to five submissions per author and retain the 200 most
   recent annotated eligible posts. Seven further annotated posts passing
   that cap remain unused. Selection decisions are saved in
   `selection_exclusions.json`; no label-based quota or metric-based selection
   was used.

Selected posts run from October 6 through October 25, 2026. The sample contains
136 authors and nine title-only text submissions. Text lengths range from 67
to 1,195 characters. It is a short-submission sample, not a representative
sample of all r/asoiaf or all ASOIAF discussion. Author overlap across later
random splits is still possible despite the cap.

## Provenance and exact preservation

`data/source_posts.json` maps dataset row numbers to original Reddit permalinks,
IDs, authors, dates, original titles and bodies, source snapshot paths and
hashes, and text hashes. Each CSV `note` repeats the source URL and assignment
rationale. IDs, notes, and author metadata are not part of the model's text.

The model text is `title + "\n\n" + body` when a body exists, and the unchanged
title otherwise. CSV quoting preserves newlines, quotation marks, commas,
Unicode, and original Markdown. These are direct source texts, not rewritten
examples. Use the original Reddit link when citing a post.

## Reddit spot checks

Eight source pages were checked through the browser on collection day:

| ID | Result |
|---|---|
| [1xfbocz](https://www.reddit.com/r/asoiaf/comments/1xfbocz/) | Author shown deleted and body absent; excluded from labels.csv despite an archive copy. |
| [1xdrprm](https://www.reddit.com/r/asoiaf/comments/1xdrprm/) | Title and body visible; hard-case question retained. |
| [1xcs178](https://www.reddit.com/r/asoiaf/comments/1xcs178/) | Title and body visible; hard-case opinion retained. |
| [1x5o5wo](https://www.reddit.com/r/asoiaf/comments/1x5o5wo/) | Title and body visible; hard-case analysis retained. |
| [1x1tpfj](https://www.reddit.com/r/asoiaf/comments/1x1tpfj/) | Text title visible; later left out under the author cap. |
| [1xbev8c](https://www.reddit.com/r/asoiaf/comments/1xbev8c/) | Title and body visible; opinion retained. |
| [1x5vl6w](https://www.reddit.com/r/asoiaf/comments/1x5vl6w/) | Title and body visible; question retained. |
| [1x0nozz](https://www.reddit.com/r/asoiaf/comments/1x0nozz/) | Title and body visible; opinion retained. |

This is not live verification of all 200 pages. All 200 are checked against
their saved archive records. A live post can change or disappear later, and
the archive cannot establish whether every public account is a human.

## Annotation process and hard cases

All 200 rows were assigned by Codex under the taxonomy in the README. The
user requested that the assistant label everything. No row is represented as
an unaided student label, and no human review has been completed. Each note
states `pre-labeled by AI; human review pending`. The required 20-post cold
pass remains unsatisfied. An assistant label is not an independent agreement
measurement, even when accompanied by a reason.

The three hard cases and the boundary decisions are written out under
**The Dataset** in the README: the quoted skull question, the unexplained
favorite Jon quotation, and the explained interpretation of Alayne's smile.
The first is question, the second opinion, and the third analysis. The test
is the presence of an author-supplied argument, not whether the text contains
a quote or whether the annotator likes the post.

## Validation and reproduction

`collect_posts.py` retrieves and filters snapshots. `prepare_dataset.py`
selects annotated posts and writes the source ledger.
`build_labels.mjs` authors literal cell values using `@oai/artifact-tool`,
checks that the values are unchanged, and exports the required CSV without
creating an additional workbook deliverable. It requires that library in
the Node environment. Plain machine-readable CSV needs no visual formatting.

Run `python validate_dataset.py` from this repository to check:

- at least 200 rows and exactly the three required columns;
- unchanged title/body content for every row against original API records;
- matching source permalinks, IDs, and SHA-256 hashes;
- no duplicate IDs, exact/normalized texts, or identical nonempty bodies;
- all three allowed labels, complete workflow notes, no false cold-label claims;
- maximum label share at most 50% and at most five posts per author.

A separate five-word-shingle check on the final 200 posts found no pair with
Jaccard similarity above 0.45 after the explicit repeated-draft exclusions.
This reduces obvious copy leakage, but does not establish semantic
independence of posts on the same topic. `.gitattributes` prevents Git's
Windows newline conversion from changing snapshot bytes or embedded CSV text.

No model was trained, no metrics were inspected, no acceptance targets were
changed, and the student's existing notebook edits were preserved.
