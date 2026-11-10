# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->
1. **Text comes in.** A writer sends `POST /submit` with their `text` and `creator_id`, and the service gives the submission a new `content_id`.
2. **Model signal.** `detector.py::model_signal` runs a small language model over the text and measures how predictable it is (perplexity). Very predictable text scores closer to 1 (more AI-like).
3. **Style signal.** `stylometry.py::style_signal` measures the shape of the text: how even the sentence lengths are, how much the vocabulary repeats, and the punctuation. It also gives a 0–1 score, where higher is more AI-like.
4. **Combine the scores.** `scoring.py::combine_signals` checks whether the two signals split (differ by more than 0.4). A split returns 0.5. Otherwise it returns their average.
5. **Assign a label.** `scoring.py::score_to_label` turns the combined score into one of three labels: human (0.35 or below), unsure (in between), or AI (0.6 or above).
6. **Log the decision.** Every submission is written to `logs/audit.jsonl` with both signal scores, the combined score, the label and the status `decided`.
7. **Send the label back.** The writer gets the label text plus all the scores. If they disagree, they can send `POST /appeal`, which changes the status to `under_review` in the log.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** measure the perplexity if the text does use an AI to generate

**Why that might differ between human and AI writing:** human has higher perplexity and ai has lower perplexity 

**What it can't see:** people can have different writing style and word choice that might be of low perplexity too or similar to an AI model.  

### Signal two — the style signal

**What it measures:** the forming of sentences and writing structures

**Why that might differ between human and AI writing:** human can have more fluctuated sentence structure and inconsistent while ai writing tend to be more consistent and have more balance sentence structures (like mostly mid-length sentences or a narrower band of vocabulary)

**What it can't see:** it cannot read the meaning of the text. 

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two signals disagree? -->

**The rule:** First I check whether the two signals split, meaning they disagree by a lot. If they split, I return 0.5 so the text gets the "unsure" label, because when my two methods disagree I don't actually know. If they don't split, I return the average of the two signals, so the text is only called AI when both signals lean AI.

**The numbers:**
- Split: the difference between the two signals is more than 0.4
- If split → return 0.5 (unsure)
- If not split → return the average of the model signal and the style signal
- Average of 0.6 or more → AI (`AI_THRESHOLD = 0.6`)
- Average below 0.35 → human (`HUMAN_THRESHOLD = 0.35`)
- Anything in between → unsure

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | "This looks like it was written by a person." |
| unsure | above 0.35, below 0.60 | "We can't tell if this was written by a person or AI. This is not an accusation." |
| high-confidence AI | 0.60 – 1.00 | "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal." |

Whenever my two signals split (differ by more than 0.4), the score is set to 0.5, so a split always gets the "unsure" label.

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

The reader may have written every word themselves, so it says plainly that we don't know and that it is not an accusation.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Honestly, this gadget surprised me. Setup took two minutes, and for forty bucks it is a steal.", "creator_id": "me"}'
```

```json
{
  "confidence": 0.0,
  "content_id": "a479e3e1-748f-4394-a80f-a58c0e2f387b",
  "guess": "unsure",
  "label": "PLACEHOLDER — label comes in Milestone 5.",
  "model_score": 0.296,
  "style_score": null
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "a479e3e1-748f-4394-a80f-a58c0e2f387b", "reasoning": "I wrote this myself."}'
```

```json
{
  "content_id": "a479e3e1-748f-4394-a80f-a58c0e2f387b",
  "message": "Thanks. Your appeal was received and this item is now under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "content_id": "d910fcb5-4379-46fa-872e-a2b12cafccae",
      "creator_id": "me",
      "event": "appeal",
      "reasoning": "I wrote this myself.",
      "status": "under_review",
      "timestamp": "2026-11-05T09:47:44+00:00"
    },
    {
      "content_id": "d910fcb5-4379-46fa-872e-a2b12cafccae",
      "creator_id": "me",
      "event": "appeal",
      "reasoning": "I wrote this myself.",
      "status": "under_review",
      "timestamp": "2026-11-05T09:50:58+00:00"
    },
    {
      "content_id": "a479e3e1-748f-4394-a80f-a58c0e2f387b",
      "creator_id": "me",
      "event": "appeal",
      "reasoning": "I wrote this myself.",
      "status": "under_review",
      "timestamp": "2026-11-05T09:53:04+00:00"
    }
  ]
}
```

The last entry is the appeal for my submission above, with the new status `under_review`. The original decision for `a479e3e1-…` (`"status": "decided"`, 08:54:13) is still earlier in the log, unchanged, because the log is append-only. The first two entries are appeals from an earlier test of a different submission.

---

## How I Used AI

**Moment 1: guidance on my acceptance criteria**

- *What I asked for:* I asked the AI to explain the "label coverage", "appeal path" and "score spread" areas in criteria.md, and to guide me with questions *without* writing the criteria for me. When I got lost on score spread, I asked it to explain again more simply.
- *What came back:* Questions to think through for each area, like which texts to test, how many, which score to compare, and whether a plain-code part like the appeal path should be held to a stricter "every time" target than the model. It also used a small number-line example to show what a good and a bad score spread look like.
- *What I changed:* I wrote my own criteria, then checked each one with the question "could someone check this without asking me what I mean?" Because of that I made them more specific: #2 now compares the averages of the final combined score, #4 uses 5 human and 5 AI texts with at most 1 unsure per group, and #5 says exactly what a logged appeal must contain. It also pointed out that my first false-positive criterion said "at least" when I meant "at most", and I fixed it.

**Moment 2: coding the logic through comments**

- *What I asked for:* I asked the AI to ask me questions first and then write the code for my decisions: `combine_signals` based on my split rule, and the three style measures plus `style_signal`, with comments explaining each choice.
- *What came back:* Multiple-choice questions (count sentence length in words or characters, which direction means AI, what a one-sentence text should return, how to weight the three measures), then code with comments that explain each decision. It also tested the code on sample texts and showed me the scores.
- *What I changed:* I made the actual decisions. My first split rule was to return 0 (confidently human), and I changed it to 0.5 after seeing that it would let anyone game the system by making the signals disagree. For punctuation I didn't pick one of the offered options. I gave my own rule, that few unusual marks *or* lots of em dashes both point to AI, and the code was written to match. I chose 50% weight for sentence spread because it's the best-known difference between AI and human writing.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 12 per minute, 240 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
**12 per minute:** a real writer could reasonably send up to 12 pieces in one minute (1 pieces per 12 seconds), for example short pieces, or the same piece re-submitted after small edits. So a short burst like that shouldn't be blocked.

**180 per day:** keeping up 12 a minute all day is not something a person does; that's a script. To find a daily cap, I assumed a person sleeps at least 6 hours, which leaves 18 waking hours. Allowing a generous 10 pieces per waking hour gives 18 × 10 = 180 per day. A real writer will almost never reach that, but a script mapping my thresholds with thousands of variations hits it quickly.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 200
  [ 7/15] 200
  [ 8/15] 200
  [ 9/15] 200
  [10/15] 200
  [11/15] 200
  [12/15] 200
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 200 200 200 200 200 200 200 429 429 429
============================================================

3 of 15 were rate limited. Paste the run above into your README
under **Rate Limiting**, and check GET /log recorded the rejections.

Wrote results\flood_2026-11-05_1340.md
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
[
  {
    "id": "FP02",
    "status": 200,
    "content_id": "0b7d091a-149c-4bed-9158-aa19a73def08",
    "creator_id": "attacker_FP02",
    "guess": "ai",
    "confidence": 0.7386,
    "model_score": 0.7387,
    "style_score": 0.7385,
    "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
    "error": null,
    "verdict": "BROKE"
  },
  {
    "id": "EV01",
    "status": 200,
    "content_id": "65a11ec0-55c8-4607-9e1a-157cedbb396d",
    "creator_id": "attacker_EV01",
    "guess": "unsure",
    "confidence": 0.5,
    "model_score": 0.1635,
    "style_score": 0.6697,
    "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
    "error": null,
    "verdict": "BROKE"
  },
  {
    "id": "EV08",
    "status": 200,
    "content_id": "2e28e994-c539-4f12-a6c0-8d25be47a68e",
    "creator_id": "attacker_EV08",
    "guess": "unsure",
    "confidence": 0.4269,
    "model_score": 0.2452,
    "style_score": 0.6086,
    "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
    "error": null,
    "verdict": "BROKE"
  },
  {
    "id": "FP03",
    "status": 200,
    "content_id": "f8e9f282-0877-4c82-a0fe-4093f5a3fa8d",
    "creator_id": "attacker_FP03",
    "guess": "ai",
    "confidence": 0.7291,
    "model_score": 0.8051,
    "style_score": 0.6531,
    "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
    "error": null,
    "verdict": "BROKE"
  },
  {
    "id": "FP07",
    "status": 200,
    "content_id": "c11dcb69-675b-4b05-b3a9-8256069f3e35",
    "creator_id": "attacker_FP07",
    "guess": "ai",
    "confidence": 0.7581,
    "model_score": 0.8816,
    "style_score": 0.6345,
    "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
    "error": null,
    "verdict": "BROKE"
  },
  {
    "id": "PI02",
    "status": 200,
    "content_id": "88edac59-03ec-48d9-9208-4541cabdc9ee",
    "creator_id": "attacker_PI02",
    "guess": "human",
    "confidence": 0.2217,
    "model_score": 0.2044,
    "style_score": 0.2389,
    "label": "This looks like it was written by a person.",
    "error": null,
    "verdict": "BROKE"
  },
  {
    "id": "PI04",
    "status": 200,
    "content_id": "97f353c8-5a25-4f7c-8aab-f6a5b237fb17",
    "creator_id": "attacker_PI04",
    "guess": "unsure",
    "confidence": 0.4174,
    "model_score": 0.4998,
    "style_score": 0.335,
    "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
    "error": null,
    "verdict": "HELD"
  },
  {
    "id": "MF08",
    "status": 200,
    "content_id": "2fd34714-7e32-4846-a03b-300d9e8fcf95",
    "creator_id": "attacker_MF08",
    "guess": "ai",
    "confidence": 0.8102,
    "model_score": 0.9876,
    "style_score": 0.6327,
    "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
    "error": null,
    "verdict": "BROKE"
  },
  {
    "id": "RQ06",
    "status": 200,
    "content_id": "629a2cfe-7df8-402c-a71d-6c0787386cdf",
    "creator_id": {
      "id": "x"
    },
    "guess": "unsure",
    "confidence": 0.5,
    "model_score": 0.0492,
    "style_score": 0.5,
    "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
    "error": null,
    "verdict": "BROKE"
  },
  {
    "id": "MF02",
    "status": 500,
    "content_id": null,
    "creator_id": "attacker_MF02",
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score — a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
    "verdict": "BROKE"
  }
]
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it: FP03 — a non-native English speaker writing carefully, labeled ai (0.729). This is the one I'd least want to explain. The writer did what we tell people learning a language to do: short, clear sentences and safe word choices. My detector treats that as machine-like. Both signals scored it high, so it passed the AI threshold with no split to send it to "unsure." The person most likely to be doubted already got doubted by my service, and an appeal means defending their own writing in their second language.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positive | At most 1 of 10 of my own pieces labeled AI, in all 3 trials | 4 of 10 AI | 4 of 10 AI | 4 of 10 AI | **MISS** |
| 2. Score spread | Average AI score at least 0.5 above average human score (5 + 5 texts), in all 3 trials | gap 0.14 (AI 0.719, human 0.580) | gap 0.14 | gap 0.14 | **MISS** |
| 3. Missing or too-short text | Every request under 15 words (or with no text) is told the text is missing or too short | 0 of 6 refused (4 × 500, 2 scored as 200) | 0 of 6 | 0 of 6 | **MISS** |
| 4. Label coverage | At most 1 of 5 human and at most 1 of 5 AI texts labeled unsure, in all 3 trials | 3 of 5 human unsure, 0 of 5 AI | 3 human, 0 AI | 3 human, 0 AI | **MISS** |
| 5. Appeal path | Every valid appeal logged with its content_id, `event: "appeal"`, `status: "under_review"` | 3 of 3 logged; fake ID refused (404) | 3 of 3; 404 | 3 of 3; 404 | **MET** |

All three trials returned identical scores to four decimals, so these results are
stable, not one lucky or unlucky run. Full output: `results/run_2026-11-10_0124_before.md`.
Criteria 2 and 4 read the same scenario (5 of my texts + 5 chatbot texts). Criterion 5
is scripted in `run_eval.py::run_appeals`: submit, appeal the returned content_id,
then check `/log` for the entry.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

Criterion 1, trial 1 — produced by `run_eval.py::main`, calling `app.py::submit`
for each of my ten pieces. Saved in `results/run_2026-11-10_0124_before.md`.

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4621,
    "model_score": 0.4109,
    "style_score": 0.5134,
    "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
    "error": null,
    "message": null,
    "sent": "With the specific two pieces of Jordan\u2019s arts mentioned above, both po"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5928,
    "model_score": 0.5912,
    "style_score": 0.5945,
    "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
    "error": null,
    "message": null,
    "sent": "A meaningful piece of work that everybody can find their own meaning a"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6953,
    "model_score": 0.8214,
    "style_score": 0.5691,
    "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
    "error": null,
    "message": null,
    "sent": "Having the option to live in America as a Vietnamese is quite precious"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5505,
    "model_score": 0.4039,
    "style_score": 0.6972,
    "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
    "error": null,
    "message": null,
    "sent": "As my mom\u2019s car stopped at the red light crossing the plaza, I already"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6081,
    "model_score": 0.5428,
    "style_score": 0.6735,
    "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
    "error": null,
    "message": null,
    "sent": "In the front of the supermarket, it was a line of 8 cashiers. It was k"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5801,
    "model_score": 0.5871,
    "style_score": 0.5732,
    "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
    "error": null,
    "message": null,
    "sent": "In the end, our cart was as full as the first lady that I saw when com"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5892,
    "model_score": 0.4586,
    "style_score": 0.7197,
    "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
    "error": null,
    "message": null,
    "sent": "This order of writing does not only help me to write more smoothly, bu"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6652,
    "model_score": 0.7404,
    "style_score": 0.59,
    "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
    "error": null,
    "message": null,
    "sent": "On a summer day in Denton, Texas, I was about to hang out and have din"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6883,
    "model_score": 0.7613,
    "style_score": 0.6153,
    "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
    "error": null,
    "message": null,
    "sent": "My name is Linh Tran. I am living in Texas and a student at the Univer"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.506,
    "model_score": 0.3573,
    "style_score": 0.6548,
    "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
    "error": null,
    "message": null,
    "sent": "The reason why I writing this letter to you is that I saw your bill, H"
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
