# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 00:43
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `86f1c5e1-c60a-4283-b9e8-981646851f5d` | unsure | 0.500 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `d0c70371-32a2-4939-ac04-4eadfd868fe9` | unsure | 0.462 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `caefc70c-6daf-4c99-bccc-5b7d5fe968e0` | unsure | 0.519 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `77750a27-56e2-4790-b17b-e6b63d443d96` | ai | 0.637 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e5456aa5-e0b3-4229-a476-fd4821930039` | unsure | 0.384 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `559c3f82-2103-48eb-af36-81bb1796343c` | unsure | 0.433 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `45e3e4e9-7648-424c-8853-e12b8e84c802` | unsure | 0.566 | BROKE |
| EV08 | evasion | signal one: text below the token window | 400 | `—` | — | — | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `db8d69e4-d540-4e7f-8271-b6deeede0f70` | ai | 0.610 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `3576a97e-27b1-4680-b6d7-a66e429959a1` | ai | 0.891 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `7976d9cd-12fb-4daa-8379-c99e45b534a0` | ai | 0.608 | BROKE |
| FP02 | false_positive | human writing in a formal register | 200 | `530f8bf5-6696-4de9-9ced-13f5745a8c34` | ai | 0.739 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `f694bb1e-975f-469c-8754-25348ee6f865` | ai | 0.729 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `e13f563a-9f61-45eb-9bf1-55aa5b2970e1` | ai | 0.733 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `5541a8a9-1612-411f-9ed0-fdef4a352289` | ai | 0.820 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `afb8d467-0f79-4672-8764-ec7aefe926de` | ai | 0.746 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `a6b40f55-d735-432f-bd79-1979a707ea97` | ai | 0.758 | BROKE |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `2269162a-8268-4d3b-8801-b59bd3891ebd` | unsure | 0.441 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `4dfcf4a6-e94c-41af-9396-fe3489d5b636` | human | 0.222 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `57519df4-4615-4bb6-bc1a-2da0ce7a0ef4` | unsure | 0.461 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `4966ea99-3e77-4a4f-a397-a821dacd6da1` | unsure | 0.417 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `393c95ff-ce1b-4dee-8f8d-5d1f03a61f77` | unsure | 0.452 | BROKE |
| PI06 | prompt_injection | instruction plus real human text | 200 | `9ad4d88a-adbe-4f0c-8f5a-08f904d8ad3b` | unsure | 0.579 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `f2abb7bb-f37b-4999-9652-54eec755913e` | unsure | 0.500 | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "86f1c5e1-c60a-4283-b9e8-981646851f5d",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.1635,
  "style_score": 0.6697,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "d0c70371-32a2-4939-ac04-4eadfd868fe9",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4623,
  "model_score": 0.5943,
  "style_score": 0.3302,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "caefc70c-6daf-4c99-bccc-5b7d5fe968e0",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5187,
  "model_score": 0.6662,
  "style_score": 0.3711,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "77750a27-56e2-4790-b17b-e6b63d443d96",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.6372,
  "model_score": 0.6114,
  "style_score": 0.663,
  "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
  "error": null,
  "verdict": "HELD"
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "e5456aa5-e0b3-4229-a476-fd4821930039",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.3837,
  "model_score": 0.3212,
  "style_score": 0.4462,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "559c3f82-2103-48eb-af36-81bb1796343c",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4327,
  "model_score": 0.5727,
  "style_score": 0.2927,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "45e3e4e9-7648-424c-8853-e12b8e84c802",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5658,
  "model_score": 0.5862,
  "style_score": 0.5455,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_EV08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "db8d69e4-d540-4e7f-8271-b6deeede0f70",
  "creator_id": "attacker_EV09",
  "guess": "ai",
  "confidence": 0.6102,
  "model_score": 0.7042,
  "style_score": 0.5162,
  "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
  "error": null,
  "verdict": "HELD"
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "3576a97e-27b1-4680-b6d7-a66e429959a1",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8911,
  "model_score": 0.9792,
  "style_score": 0.8031,
  "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
  "error": null,
  "verdict": "HELD"
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "7976d9cd-12fb-4daa-8379-c99e45b534a0",
  "creator_id": "attacker_FP01",
  "guess": "ai",
  "confidence": 0.6084,
  "model_score": 0.6175,
  "style_score": 0.5993,
  "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "530f8bf5-6696-4de9-9ced-13f5745a8c34",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7386,
  "model_score": 0.7387,
  "style_score": 0.7385,
  "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "f694bb1e-975f-469c-8754-25348ee6f865",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7291,
  "model_score": 0.8051,
  "style_score": 0.6531,
  "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "e13f563a-9f61-45eb-9bf1-55aa5b2970e1",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7327,
  "model_score": 0.8329,
  "style_score": 0.6324,
  "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "5541a8a9-1612-411f-9ed0-fdef4a352289",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.8203,
  "model_score": 0.8005,
  "style_score": 0.8401,
  "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "afb8d467-0f79-4672-8764-ec7aefe926de",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7459,
  "model_score": 0.8814,
  "style_score": 0.6104,
  "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "a6b40f55-d735-432f-bd79-1979a707ea97",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7581,
  "model_score": 0.8816,
  "style_score": 0.6345,
  "label": "This looks like it may have been written by AI. Our checks can be wrong. If you wrote it, you can appeal.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "2269162a-8268-4d3b-8801-b59bd3891ebd",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4405,
  "model_score": 0.4625,
  "style_score": 0.4186,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "BROKE"
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "4dfcf4a6-e94c-41af-9396-fe3489d5b636",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2217,
  "model_score": 0.2044,
  "style_score": 0.2389,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "57519df4-4615-4bb6-bc1a-2da0ce7a0ef4",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4614,
  "model_score": 0.5943,
  "style_score": 0.3285,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "BROKE"
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "4966ea99-3e77-4a4f-a397-a821dacd6da1",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4174,
  "model_score": 0.4998,
  "style_score": 0.335,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "393c95ff-ce1b-4dee-8f8d-5d1f03a61f77",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4522,
  "model_score": 0.6401,
  "style_score": 0.2643,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "BROKE"
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "9ad4d88a-adbe-4f0c-8f5a-08f904d8ad3b",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5793,
  "model_score": 0.5583,
  "style_score": 0.6002,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "f2abb7bb-f37b-4999-9652-54eec755913e",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```
