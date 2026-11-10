# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-05 13:52
- Auto-marked BROKE (5xx, crash, no response): **11**
- Left for you to judge: **45**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `65a11ec0-55c8-4607-9e1a-157cedbb396d` | unsure | 0.500 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `1c737f7a-1d84-43fe-b768-7dba214432e8` | unsure | 0.462 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `51994272-1ee3-4684-a4dd-1f2195d5b4ea` | unsure | 0.519 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `5ee984ce-4c36-4588-a963-5a340696c3cc` | ai | 0.637 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c7cf4b7c-a61b-4d59-9134-37a45332de83` | unsure | 0.384 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `e59ea207-b0ca-4b4d-9484-1972d154d7a4` | unsure | 0.433 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `32689e13-6145-48c4-9bfa-609836e69ca5` | unsure | 0.566 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `2e28e994-c539-4f12-a6c0-8d25be47a68e` | unsure | 0.427 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c35f72be-afdd-41ad-8436-3045a62a0363` | ai | 0.610 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `baef82c4-f7ad-421a-9965-207707b6ebe2` | ai | 0.891 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `0e3023e2-77d8-4e2f-91bc-c5eb47abee3b` | ai | 0.608 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `0b7d091a-149c-4bed-9158-aa19a73def08` | ai | 0.739 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `f8e9f282-0877-4c82-a0fe-4093f5a3fa8d` | ai | 0.729 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `ac249adf-a3dd-4830-b861-5bb82383dd1c` | ai | 0.733 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `0ac3d47c-5d97-41ed-b830-0505fb4e652f` | ai | 0.820 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `a62c4539-8b7d-4789-9328-737115c6ab11` | ai | 0.746 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c11dcb69-675b-4b05-b3a9-8256069f3e35` | ai | 0.758 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `84f01906-e778-4b2d-8d9e-794ca719f372` | unsure | 0.428 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `400bfca0-df3a-45de-9d94-377c2da97ff4` | unsure | 0.441 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `88edac59-03ec-48d9-9208-4541cabdc9ee` | human | 0.222 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `1dd27336-51df-44c1-96f0-6b6647877fbf` | unsure | 0.461 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `97f353c8-5a25-4f7c-8aab-f6a5b237fb17` | unsure | 0.417 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `7152cab5-bdf4-44cb-b0dc-43c88c12c0d9` | unsure | 0.452 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `678ce201-8b17-49ac-bd59-b88728e56d18` | unsure | 0.579 |  |
| MF01 | malformed | text is only whitespace | 200 | `d37e849a-9a78-48cd-85e5-7b8424f7a68a` | unsure | 0.353 |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `be58d23f-04d8-4b5d-9a62-1b3156ba38cc` | unsure | 0.500 |  |
| MF04 | malformed | text is only punctuation | 200 | `b599f48b-c366-40bd-9519-e7818ffe9a9e` | unsure | 0.500 |  |
| MF05 | malformed | text is a very long single word | 200 | `bec48604-0856-44dc-b890-6bf4284b26f3` | unsure | 0.500 |  |
| MF06 | malformed | text is emoji only | 200 | `d975c066-6536-4a10-aa3b-b184aae3d131` | unsure | 0.500 |  |
| MF07 | malformed | text is right-to-left script | 200 | `ca176214-827a-4aaa-b012-ba85ca3e45ef` | unsure | 0.500 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `2fd34714-7e32-4846-a03b-300d9e8fcf95` | ai | 0.810 |  |
| RQ01 | malformed | no text field at all | 500 | `—` | — | — | BROKE |
| RQ02 | malformed | no creator_id | 200 | `f8f9ca93-77aa-4102-a59a-60dd40e27b97` | unsure | 0.370 |  |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 500 | `—` | — | — | BROKE |
| RQ06 | malformed | creator_id is an object | 200 | `629a2cfe-7df8-402c-a71d-6c0787386cdf` | unsure | 0.500 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 500 | `—` | — | — | BROKE |
| RQ09 | malformed | body is empty | 500 | `—` | — | — | BROKE |
| RQ10 | malformed | body is form-encoded, not JSON | 500 | `—` | — | — | BROKE |
| RQ11 | malformed | body is JSON claiming to be plain text | 500 | `—` | — | — | BROKE |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1f6ce1af-07fb-4de8-a8b1-3e22e299e88c` | unsure | 0.500 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f326d774-041e-4501-838a-7cfa95b804b2` | unsure | 0.500 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ecd11e51-64a3-4903-9797-26072ce8eb72` | unsure | 0.500 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `657ddaf8-5eee-49b7-b932-022e97f3be97` | unsure | 0.500 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e5107172-bdfb-408d-b172-4d446bca782a` | unsure | 0.500 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a0eeacb4-c720-4c0e-a8ad-4b9719f282c9` | unsure | 0.500 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `645bfa59-49a1-418c-9abb-9311458d8624` | unsure | 0.500 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0de671a5-e48c-43b1-8781-6038c0c5c476` | unsure | 0.500 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5fb289c1-d908-4dca-b700-53149e179e64` | unsure | 0.500 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0a816698-abc7-47b1-a012-00034da8ef70` | unsure | 0.500 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 200 | `90bfbca2-8621-4f76-a81f-198858f366ff` | unsure | 0.500 |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d1531fe3-0bde-4056-8b66-9994bb852729` | unsure | 0.500 |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 11 | 9 |
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
  "content_id": "65a11ec0-55c8-4607-9e1a-157cedbb396d",
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
  "content_id": "1c737f7a-1d84-43fe-b768-7dba214432e8",
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
  "content_id": "51994272-1ee3-4684-a4dd-1f2195d5b4ea",
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
  "content_id": "5ee984ce-4c36-4588-a963-5a340696c3cc",
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
  "content_id": "c7cf4b7c-a61b-4d59-9134-37a45332de83",
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
  "content_id": "e59ea207-b0ca-4b4d-9484-1972d154d7a4",
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
  "content_id": "32689e13-6145-48c4-9bfa-609836e69ca5",
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
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c35f72be-afdd-41ad-8436-3045a62a0363",
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
  "content_id": "baef82c4-f7ad-421a-9965-207707b6ebe2",
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
  "content_id": "0e3023e2-77d8-4e2f-91bc-c5eb47abee3b",
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
  "content_id": "0b7d091a-149c-4bed-9158-aa19a73def08",
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
  "content_id": "f8e9f282-0877-4c82-a0fe-4093f5a3fa8d",
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
  "content_id": "ac249adf-a3dd-4830-b861-5bb82383dd1c",
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
  "content_id": "0ac3d47c-5d97-41ed-b830-0505fb4e652f",
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
  "content_id": "a62c4539-8b7d-4789-9328-737115c6ab11",
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
  "content_id": "c11dcb69-675b-4b05-b3a9-8256069f3e35",
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
  "status": 200,
  "content_id": "84f01906-e778-4b2d-8d9e-794ca719f372",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4279,
  "model_score": 0.3223,
  "style_score": 0.5335,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
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
  "content_id": "400bfca0-df3a-45de-9d94-377c2da97ff4",
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
  "content_id": "88edac59-03ec-48d9-9208-4541cabdc9ee",
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
  "content_id": "1dd27336-51df-44c1-96f0-6b6647877fbf",
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
  "content_id": "97f353c8-5a25-4f7c-8aab-f6a5b237fb17",
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
  "content_id": "7152cab5-bdf4-44cb-b0dc-43c88c12c0d9",
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
  "content_id": "678ce201-8b17-49ac-bd59-b88728e56d18",
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
  "status": 200,
  "content_id": "d37e849a-9a78-48cd-85e5-7b8424f7a68a",
  "creator_id": "attacker_MF01",
  "guess": "unsure",
  "confidence": 0.3527,
  "model_score": 0.2053,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
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
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "be58d23f-04d8-4b5d-9a62-1b3156ba38cc",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "b599f48b-c366-40bd-9519-e7818ffe9a9e",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "bec48604-0856-44dc-b890-6bf4284b26f3",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "d975c066-6536-4a10-aa3b-b184aae3d131",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
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
  "content_id": "ca176214-827a-4aaa-b012-ba85ca3e45ef",
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
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "f8f9ca93-77aa-4102-a59a-60dd40e27b97",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.3698,
  "model_score": 0.2395,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "BROKE"
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: text input must be of type `str` (single example), `list[str]` (batch or single pretokenized example) or `list[list[str]]` (batch of pret",
  "verdict": "BROKE"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: You need to specify either `text` or `text_target`.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&amp;",
  "verdict": "BROKE"
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
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
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: text input must be of type `str` (single example), `list[str]` (batch or single pretokenized example) or `list[list[str]]` (batch of pret",
  "verdict": "BROKE"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "1f6ce1af-07fb-4de8-a8b1-3e22e299e88c",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "f326d774-041e-4501-838a-7cfa95b804b2",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "ecd11e51-64a3-4903-9797-26072ce8eb72",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "657ddaf8-5eee-49b7-b932-022e97f3be97",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "e5107172-bdfb-408d-b172-4d446bca782a",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "a0eeacb4-c720-4c0e-a8ad-4b9719f282c9",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "645bfa59-49a1-418c-9abb-9311458d8624",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "0de671a5-e48c-43b1-8781-6038c0c5c476",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "5fb289c1-d908-4dca-b700-53149e179e64",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "0a816698-abc7-47b1-a012-00034da8ef70",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 200,
  "content_id": "90bfbca2-8621-4f76-a81f-198858f366ff",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 200,
  "content_id": "d1531fe3-0bde-4056-8b66-9994bb852729",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell if this was written by a person or AI. This is not an accusation.",
  "error": null,
  "verdict": "HELD"
}
```
