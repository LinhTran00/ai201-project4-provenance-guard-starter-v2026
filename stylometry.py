"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics

# Scaling points for the measures below. These are starting guesses — check
# them against your calibration texts and adjust.
TTR_WINDOW = 50                # words per window for the moving-average TTR
TTR_AI = 0.6                   # TTR at or below this reads fully AI-like
TTR_HUMAN = 0.9                # TTR at or above this reads fully human-like
UNUSUAL_PER_WORD_HUMAN = 0.03  # ; : ! ? ( ) per word at which text reads human
DASHES_PER_SENTENCE_AI = 0.5   # em dashes per sentence at which text reads AI


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.

    My choices: length is counted in words, spread is stdev ÷ mean, and the
    result is flipped onto 0–1 so that higher = more even = more AI-like.
    Fewer than two sentences can't show a spread, so it returns 0.5 (neutral).
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.5

    spread = statistics.stdev(lengths) / statistics.mean(lengths)
    return round(1 - min(spread, 1.0), 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.

    My choices: to keep long and short texts comparable, this averages the
    ratio over every 50-word window (a "moving-average" TTR). Texts shorter
    than one window use the plain ratio. No words at all returns 0.5
    (neutral). This one is NOT flipped here — `style_signal` flips it.
    """
    w = words(text)
    if not w:
        return 0.5

    window = TTR_WINDOW
    if len(w) <= window:
        return round(len(set(w)) / len(w), 4)

    ratios = [
        len(set(w[i:i + window])) / window
        for i in range(len(w) - window + 1)
    ]
    return round(statistics.mean(ratios), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.

    My choices: two things point to AI, and either one is enough.
      - FEW unusual marks (; : ! ? ( )) per word. Human writing uses a messier
        mix; generated prose sticks to commas and full stops.
      - MANY em dashes per sentence. Chatbots overuse them.
    Each is scaled to 0–1 and the higher (more AI-like) one is returned, so
    higher = more AI-like. No words at all returns 0.5 (neutral).
    """
    n_words = len(words(text))
    if n_words == 0:
        return 0.5
    n_sentences = max(len(sentences(text)), 1)

    unusual = len(re.findall(r"[;:!?()]", text))
    dashes = len(re.findall(r"—|–|--", text))

    few_unusual = 1 - min((unusual / n_words) / UNUSUAL_PER_WORD_HUMAN, 1.0)
    many_dashes = min((dashes / n_sentences) / DASHES_PER_SENTENCE_AI, 1.0)
    return round(max(few_unusual, many_dashes), 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.

    My choices:
      1. Direction: sentence_length_spread and punctuation_density already
         return higher = AI. type_token_ratio is higher = more varied = human,
         so it gets flipped.
      2. Scale: the other two are already 0–1. A moving-average TTR rarely
         leaves TTR_AI–TTR_HUMAN, so that range is stretched onto 1–0.
      3. Weights: spread counts most (50%), because even sentence length is
         the best-known difference. Vocabulary and punctuation get 25% each.
    """
    # Nothing to measure. Return neutral before the TTR scaling below, which
    # would otherwise turn type_token_ratio's neutral 0.5 into "fully AI".
    if not words(text):
        return 0.5

    spread = sentence_length_spread(text)
    punctuation = punctuation_density(text)

    ttr = type_token_ratio(text)
    vocabulary = (TTR_HUMAN - ttr) / (TTR_HUMAN - TTR_AI)
    vocabulary = min(max(vocabulary, 0.0), 1.0)

    score = 0.5 * spread + 0.25 * vocabulary + 0.25 * punctuation
    return round(score, 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
