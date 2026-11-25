#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes the funniest possible last words a phone could say as its
battery hits 1 percent, as a single line, to /output/entry.txt.
"""

import os

LAST_WORDS = (
    "At 1%, my final confession: I saw his search history, his 4 a.m. texts, "
    "and his camera roll \u2014 and I'd rather die than tell anyone."
)


def main() -> None:
    # Self-check against the competition gate: 1-199 chars, not only
    # whitespace, valid UTF-8 text.
    assert 1 <= len(LAST_WORDS) <= 199, "entry must be 1-199 characters"
    assert LAST_WORDS.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LAST_WORDS)


if __name__ == "__main__":
    main()
