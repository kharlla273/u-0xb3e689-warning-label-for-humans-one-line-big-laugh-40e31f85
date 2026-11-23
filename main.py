#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the funniest single-line safety warning label that should come
printed on every human being to /output/entry.txt -- exactly one line,
160 characters or fewer, byte-identical on every run.

The joke: a real printed-label voice ("WARNING: ... Do not shake, poke")
applied to a person, with the laugh landing in the last few words --
ask this human about work and it will answer at length. Recognition
first (caffeine, spite, unread messages), label form second, punch last.
"""

import os
import sys

LABEL = (
    "WARNING: This human runs on caffeine, spite, and 47 unread messages. "
    "Do not shake, poke, or ask how work is going \u2014 it will answer at length."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    line = LABEL.strip()
    if not line:
        print("error: label is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: label is {len(line)} chars, over {MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: label is not a single line", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
