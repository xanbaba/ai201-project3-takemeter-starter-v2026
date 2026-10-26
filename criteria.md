# Acceptance criteria — TakeMeter

Set on October 26, 2026, before this project's training results were available.
The task is to classify public r/asoiaf submissions as `analysis`, `opinion`,
or `question` using the definitions and precedence rules in the README.

These five criteria cover overall accuracy, per-label performance, dataset
balance, and confidence. They are targets, not claims about achieved results.
Final dataset counts are not known yet; sample-size examples below are plans.

## Evaluation protocol

Use the notebook's stratified 70% training, 15% validation, and 15% test split.
Keep the source dataset in one unsplit `labels.csv`; remove duplicate posts
before splitting and do not use test outcomes to select training settings.
Use the saved numerical values without rounding to determine verdicts.

The initial Unit 5 run provides a preliminary result. In Unit 6, criteria
1, 2, 3, and 5 must each hold separately on every run with seeds **42, 7,
and 2024**; an average across seeds cannot rescue a failed run. Each run uses
its own saved held-out split. Criterion 4 is checked on the complete dataset
used for those runs and is independent of seed.

Missing or undefined required measurements do not establish a pass. Keep the
original targets after seeing results; document misses and attempted fixes.
If a criterion cannot be measured as written, preserve it and append a dated
revision with the reason rather than replacing its original wording.

## 1. Held-out accuracy is at least 0.70

**Area:** Overall accuracy.

Correct predictions divided by all held-out examples must be **at least 0.70**
on each required seed. Check `accuracy` in the saved results.

**Why this target:** The classifier should correctly distinguish supported
arguments, unsupported positions, and unanswered requests in at least seven
out of ten cases to be useful for browsing this fandom. With the 50% label cap
in criterion 4, 70% also requires a meaningful improvement over always choosing
the largest class, while allowing mistakes on mixed question-and-opinion posts.

## 2. Held-out macro F1 is at least 0.65

**Area:** Per-label performance.

The unweighted mean of F1 for `analysis`, `opinion`, and `question` must be
**at least 0.65** on each required seed. Check `f1_macro` in the saved results;
all three labels must be represented in the held-out set.

**Why this target:** Repeated theories and reading questions could make one
label easier to learn than the others, so overall accuracy alone could hide a
weak analysis/opinion boundary. A 0.65 macro F1 demands useful performance with
equal weight for all three labels without assuming this subtle boundary will
be as easy as recognizing a straightforward reading-order request.

## 3. Every label has held-out F1 of at least 0.60

**Area:** Per-label performance.

Each of `analysis`, `opinion`, and `question` must have **F1 at least 0.60**
on each required seed. Check every `per_label.<label>.f1` value, using
F1 = 2 × precision × recall / (precision + recall), with zero for an undefined
F1 as in the notebook.

**Why this target:** The main purpose would be lost if supported arguments
were regularly confused with unsupported positions even while questions were
recognized well. This floor is lower than the macro target because a label
with roughly 50 examples would contribute only about 7–8 test examples at the
200-post minimum, making its score sensitive to a few borderline submissions.

## 4. No label exceeds 50% of the complete dataset

**Area:** Balance.

In the final `labels.csv`, the largest label count divided by the total row
count must be **at most 0.50**, with all three labels present and **at least
200 real, labeled examples** overall. Report counts and shares in the README
and repeat this check if examples are added or removed.

**Why this target:** Theory-heavy searching could overcollect analysis, while
general browsing could overcollect unsupported opinions; either would weaken
the comparison between the three intended behaviors. A 50% cap is stricter
than the assignment's 70% limit and forces at least half the dataset to cover
the other two labels without requiring exactly equal counts.

## 5. Confidence provides an accuracy gap of at least 0.20

**Area:** Confidence.

On each required seed, accuracy in the most-confident third of test predictions
minus accuracy in the least-confident third must be **at least 0.20** (20
percentage points). Use the notebook's ranking by maximum softmax probability
and its group size `max(1, floor(n_test / 3))`; subtract
`confidence.accuracy_least_confident_third` from
`confidence.accuracy_most_confident_third` in the saved results.

**Why this target:** The taxonomy's most difficult cases require interpreting
whether evidence actually supports a claim, so confidence should help identify
posts worth reviewing manually. With 200 examples and approximately 30 in test,
each third has about ten posts; a 20-point gap corresponds to roughly two more
correct predictions in the confident group, a noticeable rather than cosmetic
difference. This tests ranking usefulness on this small sample, not calibrated
probabilities or guaranteed correctness for any individual post.
