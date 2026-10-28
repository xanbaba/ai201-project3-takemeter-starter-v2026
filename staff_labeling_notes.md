# Staff-label first pass — reviewed and accepted

This is a test run of the course by its author. On October 27, 2026, the
course author confirmed agreement with all 30 first-pass labels, before the
staff answer key was available or opened. The labels follow
`data/staff_taxonomy.md` and use the exact text in `data/staff_posts.csv`.

`my_staff_labels.csv` contains all 30 original texts, unchanged, with only
`text` and `label` columns. Counts: 11 `analysis`, 9 `hot_take`, and 10
`reaction`. These staff labels are separate from the project's
`analysis`/`opinion`/`question` taxonomy; the 200 training labels are unchanged.

## First-pass decisions

**sp_001 — `analysis`**

> Pulled the splits from the last five editions. The winning time has moved by 40 seconds total in ten years, but the 100th-place time is four minutes faster. The depth changed, the front didn't.

The winning-time change and 100th-place change across editions support the distinction between front performance and field depth.

**sp_002 — `analysis`**

> I tracked sleep against session quality for eleven weeks. Under seven hours the next day's intervals were 6-8 seconds per mile slower, every time bar one. Small sample, one runner, but it's consistent enough that I've stopped scheduling hard days after late shifts.

Eleven weeks of sleep/session records and the 6–8 second pace difference support a scheduling decision. A small sample limits the inference but does not remove its evidence.

**sp_003 — `analysis`**

> The club championship scoring changed in 2019 from top-6 to top-10. Since then our B team has finished above the A team twice. That's not depth improving, it's the scoring rewarding turnout.

The dated scoring-rule change and two B-team finishes support an explanation based on turnout incentives.

**sp_004 — `analysis`**

> Everyone blames the hill at 18 miles. I split the field into people who ran the first half under 1:45 and over, and the slowdown after 18 was almost identical for both groups. If the hill were the problem the fast starters would fall apart harder.

The comparison of slowdown between the two first-half time groups carries the argument about the hill. Whether the inference is convincing is separate from whether evidence is offered.

**sp_005 — `analysis`**

> Carbon plates aren't the whole story. My times dropped 2% in the shoes and another 2% the following year in the same pair, when the only thing that changed was going from 35 to 50 miles a week.

Two successive 2% improvements, with mileage changing in the second year while shoes stayed constant, support the claim that shoes are not the only cause.

**sp_006 — `analysis`**

> Checked the entry lists. 41% of this year's field have never run the distance before, against 26% five years ago. That's why the finish-line photos look different, not because standards dropped.

The 41% versus 26% entry-list comparison supports the explanation based on new participants.

**sp_007 — `analysis`**

> Ran the same loop in 4C and in 24C within a fortnight, same effort by heart rate. 90 seconds slower in the heat over six miles. People keep saying heat costs you 'a bit' and it's more than that.

Temperatures, the same loop, controlled heart-rate effort, and a 90-second difference support the claim about the size of heat effects. Personal experience does not override evidence under rule 3.

**sp_008 — `analysis`**

> Went back through the club results going back to 2012. Every single year the number of people who enter the spring marathon and don't start it sits between 18 and 23 percent. It's not a bad-luck year, it's the base rate.

The repeated 18–23% non-start rate since 2012 supports the base-rate explanation.

**sp_009 — `analysis`**

> The 10K route was remeasured in 2021 and came out 60 metres long. Everyone comparing PBs from before and after that is comparing two different races, which is about 12 seconds at club pace.

The 2021 remeasurement and 60-metre excess support the warning about comparing personal bests; the estimated 12 seconds quantifies its significance.

**sp_010 — `analysis`**

> Three of us ran the same session on the same day, different shoes, within 10 seconds of each other over 5 miles. I'm not saying shoes do nothing, but whatever they do was smaller than the noise between three people.

The same-day, same-session comparison of three runners within ten seconds supports the explicitly limited claim about shoe effects versus observed variation.

**sp_011 — `hot_take`**

> Anyone who races more than once a month isn't training, they're just collecting medals.

The general claim that frequent racers only collect medals has no supporting fact. Rule 2 makes this a claim about runners, rather than an immediate personal reaction.

**sp_012 — `hot_take`**

> Heart rate zones are astrology for runners.

The astrology analogy dismisses heart-rate zones without evidence or a report of a recent personal experience.

**sp_013 — `hot_take`**

> The club needs to stop pretending the Tuesday session is for everyone. It isn't and it never has been.

The claim that the Tuesday session is not for everyone is asserted without a concrete example, comparison, or other support.

**sp_014 — `analysis`**

> Times are down about 3% since the shoe rules changed, so obviously the shoes are the whole story and the sport has a problem.

Borderline: the 3% change since the shoe-rule change is explicitly connected by “so” to a causal conclusion. I read the fact as carrying the inference under rule 1, even though “the whole story” overclaims what it establishes. A hot_take reading is also defensible if “obviously” and the sweeping conclusion make the statistic decorative. This first-pass choice was accepted before staff labels were available.

**sp_015 — `hot_take`**

> Marathon training plans are all the same plan with different fonts.

The claim that all marathon plans are effectively identical is a generalization without an offered comparison or example.

**sp_016 — `hot_take`**

> If you need a gel before 90 minutes you have a fuelling problem, not an energy problem.

Ninety minutes is a threshold in the asserted rule, not an observation supporting it. The fueling diagnosis is offered without evidence.

**sp_017 — `hot_take`**

> Road racing peaked in about 2015 and everything since has been marketing.

The approximate year locates the claimed peak but does not support the claim that everything afterward was marketing.

**sp_018 — `hot_take`**

> Track sessions are wasted on anyone running slower than 8 minute miles. You'd get more out of just running more.

Eight-minute pace specifies whom the claim concerns; it is not evidence that track sessions are ineffective for those runners.

**sp_019 — `hot_take`**

> Nobody actually enjoys the long run. They enjoy having done it, which is a completely different thing, and the sport would be more honest if it said so.

The post asserts a general psychological claim about all runners without evidence. Feeling-related subject matter does not make it a report of the writer’s immediate experience.

**sp_020 — `hot_take`**

> Every injury thread on this forum is the same injury and the same three replies.

The universal claim about injury threads supplies no sampled threads or other checkable comparison.

**sp_021 — `reaction`**

> Four minutes off. FOUR. I've been chasing that time for two years and I'm sat on the kerb outside the finish just grinning at nothing.

The four-minute improvement and two-year chase frame the writer’s immediate joy at the finish; they do not support a general argument.

**sp_022 — `reaction`**

> Got up at 5, drove ninety minutes, and it's cancelled. Standing in the car park in the rain reading the email.

The time and drive length establish the writer’s just-happened cancellation experience and frustration, rather than a general claim.

**sp_023 — `reaction`**

> First run back after eight weeks out. Two miles, slower than my warm-up used to be, and I don't care even slightly.

The first run after injury and its distance frame a current personal feeling. There is no evidence-based conclusion about training or recovery.

**sp_024 — `reaction`**

> Watching the last 400 of that and I had to stand up. Still standing up actually.

The post describes the writer’s immediate physical and emotional response to watching a finish.

**sp_025 — `reaction`**

> Blew up at 20 with the pace band still in my hand like it was going to help. Rough one.

The mile marker and pace band describe the writer’s recent difficult race and disappointment, not an argument supported by data.

**sp_026 — `reaction`**

> Someone handed my kid an orange slice at mile 22 and I have been crying on and off since.

The mile marker identifies the event prompting the writer’s ongoing emotional response. The post makes no general claim.

**sp_027 — `reaction`**

> Wind was so bad on the out section I was leaning at about 20 degrees. Coming back felt like cheating.

Borderline: the out-and-back comparison describes how this run felt. The approximate leaning angle is scene-setting, not a measured premise supporting a general conclusion. Rule 3 does not turn every number into analysis.

**sp_028 — `reaction`**

> Third DNF this year. I don't really want to talk about it, just wanted to put it somewhere.

The DNF count supplies context for a personal disclosure of disappointment, without advancing an evidence-backed explanation.

**sp_029 — `reaction`**

> Just realised the shoes I set every PB in this year are the ones I bought by accident in the wrong size.

Borderline: “Just realised” centers an immediate personal discovery about accidentally bought shoes. The post offers no explicit claim about shoe sizing or performance for the personal-best detail to support.

**sp_030 — `reaction`**

> Signed up. Card's charged, no going back, immediately regret everything.

The post reports the writer’s immediate regret after registering and paying, without a general claim.

## Comparison completed — October 28, 2026

The staff file arrived after the first-pass labels were saved and accepted.
`python agreement.py` compared all 30 posts: **29 agreed, 1 disagreed (96.7%)**,
with no missing or extra posts. See `agreement_results.json` for the arithmetic
and the README Agreement Report for the full two-sided adjudication of sp_014.

The accepted `analysis` label is retained as defensible under rule 1; staff
chose `hot_take`. This is category (c), ambiguity with a defensible first-pass
reading. Totals: (a) 0, (b) 0, (c) 1. The original first-pass CSV and reasons
above remain unchanged, and agreement is not recomputed from adjudicated labels.

This separate staff exercise does not verify the 180 training annotations that
still carry human-review-pending notes.
