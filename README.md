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

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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
