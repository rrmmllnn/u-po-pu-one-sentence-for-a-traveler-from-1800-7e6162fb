#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (<=200 characters) explaining the modern
internet to someone arriving from 1800, using only things a person
from that year already knows: a road, a library, a post office, a
letter, a book. No network, no randomness: the output is identical
on every run.
"""

SENTENCE = (
    "The internet is a road of light linking distant homes to one "
    "great library and post office, where your letter reaches a friend "
    "across the world in a blink and books beyond counting wait to be read."
)


def main() -> None:
    # One sentence, one terminal full stop, within the 200-character gate.
    assert SENTENCE.count(".") == 1, "entry must be exactly one sentence"
    assert 1 <= len(SENTENCE) <= 200, f"entry is {len(SENTENCE)} characters"
    assert SENTENCE.strip() == SENTENCE, "no leading/trailing whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
