# Milestone 2: Taxonomy boundary stress test

Date: October 26, 2026

The final definitions, six real examples, and annotation rules are in
[README.md](README.md#label-taxonomy). The definitions are also copied to
`label_definitions.txt` for the later baseline. No training has been run for
this milestone, and no acceptance targets have been selected.

## AI exercise and disclosure

Codex drafted the taxonomy and generated the eight synthetic submissions below
in response to this task: "Given analysis, opinion, and question, write eight
ASOIAF submissions that sit at their boundaries, including mixed questions,
quotes without argument, and emotional evidence-backed claims. Classify each
using explicit rules and tighten any rule that leaves two outcomes."

The same assistant generated and classified the cases. This is a design
exercise, not independent model validation or measured annotator agreement.
These invented posts must never be included among the 200 real examples.

## What the exercise tightened

- Initial idea: analysis has facts, opinion has feelings, question asks things.
  Problem: a quoted line can be decorative, feelings can accompany evidence,
  and an argument can have a question as its title.
- Revision: analysis requires a claim, identifiable evidence, and a connection
  supplied by the author; neither length nor a quote alone qualifies.
- Revision: resolve overlaps with analysis, then opinion, then question.
  Reading background is not a position on the question being asked.
- Revision: a specific scene paraphrase counts without a formal citation;
  an author-attributed statement counts without opening its source link.
- Revision: any qualifying supported claim triggers analysis; counting which
  function takes up most words would create another subjective boundary.
- Dropped candidate: reaction. Emotional immediacy is difficult to establish
  from archived text and overlaps with both opinion and analysis.

## Eight synthetic boundary cases

| # | Invented submission | Label | Application of the final rule |
|---|---|---|---|
| 1 | Why do people call this a calm scene? The narration gives the characters only half a heartbeat before impact, so a long victorious pause does not fit the stated timing. | `analysis` | A question title and emotional implication do not override the timing evidence connected to an interpretation. |
| 2 | Words are wind. Anyway, the next book will definitely be the best fantasy novel ever. | `opinion` | The quotation does not support the prediction about quality. |
| 3 | I finished the five main books yesterday. Should I read the novellas or Fire & Blood next? | `question` | Reading history provides context; the writer supplies no answer or position on ordering. |
| 4 | What is your favorite theory? Mine is that every raven secretly works for the same sorcerer. I have no evidence; I just love the idea. | `opinion` | A stated speculative answer takes precedence over the request for other answers. |
| 5 | I hate this choice. Ned warns Cersei before taking steps against her, giving her time to respond; that warning helps explain why his plan fails. | `analysis` | A concrete scene event supports a causal explanation despite the emotional opening. |
| 6 | Everyone knows the novels prove the maesters control everything. Can someone please explain why people still disagree? | `opinion` | The rhetorical challenge includes a position, but the supposed evidence is not identified. |
| 7 | Tyrion calls the prince a winged lion, but I cannot work out what that means. Is there a joke I am missing? | `question` | Even a specific textual reference is only the object of the question; no interpretive answer is advanced. |
| 8 | I love these books and I am sure the ending will be brilliant. Separately, Ned's warning gives Cersei time to act, which makes it an example of mercy carrying political risk. What do you think? | `analysis` | One scene-supported interpretive claim qualifies even though other opinions lack support and the post asks for responses. |

All eight receive one label under the final precedence rule. This is a logical
check of these cases, not evidence that two independent people would agree on
all future posts. Case 7 is invented wording, not a quotation from the real
Griff discussion, and its lore accuracy is not being established here.

## Two-sided argument for the real borderline post

Post: [Reaction to Martin's writing plans](https://www.reddit.com/r/asoiaf/comments/1qn68wk/).
The author references Martin's concern about an adaptation passing the stories,
recalls a plan for as many as fifteen stories, and doubts another will appear.

**Case for analysis:** The post is not entirely evidence-free. It identifies
an attributed statement and a numerical ambition. A reader could understand
their juxtaposition as an implied argument that the plans are unrealistic.

**Case for opinion:** The post never supplies a concrete reason connecting
those plans to failure to publish. Its reaction and repeated disbelief do the
work. Treating the reader's inferred argument as the author's explanation
would make the evidence requirement depend on annotator imagination.

The README resolves this using the author-supplied connection rule. This
two-sided exercise was performed by Codex, not Claude or a breakout group.
The student's own review and a blind peer/independent-AI discussion remain
available as further checks; neither is represented as already completed.

## Submission requirements carried forward

- `criteria.md`: five numbered criteria with numeric targets and reasons,
  written and committed before training results are viewed (Milestone 3).
- `labels.csv`: at least 200 real examples with `text`, `label`, and `note`,
  in one unsplit file; no label above 70% (Milestone 4).
- `README.md`: complete What This Does, Label Taxonomy, The Dataset,
  The Training Run, and How I Used AI by submission.
- Complete training and commit `results.json` and `test_split.csv`.
- At least four new commits, using this same repository next unit.

This milestone completes the taxonomy documentation, not the whole submission.
The notebook still contains starter labels and must be aligned with these
definitions before training; existing notebook edits belong to the student.
