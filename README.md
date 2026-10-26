# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

TakeMeter will classify public discussion submissions from
[r/asoiaf](https://www.reddit.com/r/asoiaf/), a community within the A Song of
Ice and Fire fandom. It will sort submissions into `analysis`, `opinion`, and
`question` using the evidence and position expressed in the title and body.
The [community reading notes](milestone1.md) contain 30 linked submissions,
three candidate distinctions, AI-assistance disclosure, and the unresolved
assignment concern about spoilers. The student's twenty-minute reading is
still pending.



---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

The annotation unit is one human-written submission's title plus body, without
its replies, votes, username, or linked-page contents. Examples below are real
submissions from the Milestone 1 reading, with short verbatim excerpts and
linked explanations; excerpts alone are not the full training examples.
Source links contain spoilers.

### `analysis`

**Definition:** A submission that advances an interpretation, explanation,
prediction, or evaluation and explicitly connects at least one specific,
checkable passage, scene event, or attributed source statement to that claim.

**Example 1:** [Griff wordplay](https://www.reddit.com/r/asoiaf/comments/1u6lggy/)
> Tyrion is telling Griff he knows who he is already and I never picked up on it.

The body quotes the dialogue and explains how a winged lion points to Griff's
identity; the claim has evidence and an explicit connection.

**Example 2:** [Daemon's final jump](https://www.reddit.com/r/asoiaf/comments/1uojuom/)
> Half a heartbeat is less than a second.

The author uses the passage's timing to argue against a prolonged, triumphant
interpretation of the scene. Emotional language does not change the label.

### `opinion`

**Definition:** A submission that states a position, preference, emotional
judgment, or speculative answer about the discussion topic but does not connect
specific, checkable evidence to support any such claim.

**Example 1:** [Reaction to writing plans](https://www.reddit.com/r/asoiaf/comments/1qn68wk/)
> I doubt we'll see even one more.

The author's central position is disbelief about future stories; mentioning
announced plans sets the context but does not explain why those plans will fail.

**Example 2:** [Favorite ASOIAF theory](https://www.reddit.com/r/asoiaf/comments/1j3tmpk/)
> My personal favorite is that Lyanna was unknowingly a secret warg

The author supplies a substantial imagined account of character motives but
does not identify an existing scene or passage as evidence for its central
secret-warg premise. The title also asks a question; the body advances an
unsupported answer, so the position takes precedence.

### `question`

**Definition:** A submission that requests information, clarification,
recommendations, or other readers' answers without advancing its own position
or answer about that topic.

**Example 1:** [First-time reading order](https://www.reddit.com/r/asoiaf/comments/svrwnt/)
> The largest question being whether I should read Fire & Blood before or after the main series.

The writer supplies reading background and a tentative default for the main
books but does not answer the actual companion-book ordering question.

**Example 2:** [Companion-book spoilers](https://www.reddit.com/r/asoiaf/comments/3icoj0/)
> Is reading through the book The World of Ice and Fire going to spoil anything?

The writer lists previously read books and asks about spoiler coverage; that
background is not an argument or an answer to the question.

### The hardest boundary

**Which two labels:** `analysis` and `opinion`.

**Borderline real post:** [Reaction to writing plans](https://www.reddit.com/r/asoiaf/comments/1qn68wk/).
It references an author statement and a proposed number of stories, so it
contains checkable material; however, it mainly expresses disbelief without
using that material to explain the prediction. The chosen label is `opinion`.

**Decision rule to apply every time:** Identify a claim about the discussion
topic, then identify a specific passage, scene event, or attributed statement
and the author's explanation connecting it to that claim. All three must be
present for `analysis`; merely naming a character, mentioning a number, quoting
something, or saying "the books prove it" is insufficient. A clearly described
scene counts without a chapter number, and an explicit causal or comparative
connection counts without the word "because". A supported secondary claim
qualifies even if other claims are unsupported. Otherwise, a stated position
is `opinion`; if the submission only asks for answers, it is `question`.

**Mixed-post precedence:** Apply `analysis` first, then `opinion`, then
`question`. Questions in titles do not override an argument in the body.
Personal reading history and a statement of the problem are background, not
answers to it. A rhetorical question that asserts an answer counts as a
position. Evidence need only be identifiable and connected, not persuasive or
correct; this measures support offered, not canonical truth. Record suspected
misquotations or factual errors in `note` rather than silently changing labels.

**Scope:** Exclude bots, removed or duplicate submissions, image-only and
link-only content, and bare announcements/resources with neither a position
nor a request. Record exclusion reasons during collection. Read the entire
title and body before labeling; do not infer evidence from replies or links.

The [eight-case AI boundary stress test](milestone2.md) records the revisions
and a two-sided argument for the real borderline post. These definitions were
drafted with Codex; independent human agreement has not been measured.



---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:**

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->

**Counts per label:**

| Label | Count | Share |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
| **Total** |  | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**2.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**3.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:* Read the project and help scout the ASOIAF community.
- *What came back:* Codex prepared 30 linked submission observations and three
  candidate distinctions in `milestone1.md`.
- *What I changed:* The project now names r/asoiaf as its single collection
  community. My personal twenty-minute reading and review are still pending.

**Moment 2**

- *What I asked for:* Help complete Milestone 2, including real examples and
  eight AI-generated boundary cases.
- *What came back:* Codex drafted three definitions, six linked examples, a
  two-sided boundary discussion, and the stress test in `milestone2.md`.
- *What I changed:* The documented taxonomy now requires evidence to be
  explicitly connected to a claim and uses analysis/opinion/question precedence.
  Codex made these edits; I have not yet independently validated its choices.

**Pre-labelling disclosure:** Codex assigned illustrative labels to the six
real taxonomy examples and eight synthetic stress cases. No `labels.csv` has
been created or pre-labelled yet. Synthetic cases are excluded from the real
dataset; any later AI pre-labelling and my corrections will be disclosed here.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 200 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
