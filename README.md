# u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85

[![make.fun · u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/kharlla273/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/kharlla273/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Warning Label for Humans: One Line, Big Laugh — a program that writes the
funniest single-line safety warning label that should come printed on
every human being, 160 characters or fewer, to `/output/entry.txt`.

The label, in the deadpan voice of a real printed warning:

> WARNING: This human runs on caffeine, spite, and 47 unread messages. Do not shake, poke, or ask how work is going — it will answer at length.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program is deterministic: it writes the same single line on every
run, checks the line is non-empty, a single line, and at most 160
characters before writing, and exits non-zero if any check fails.

## Entry

- Competition: [Warning Label for Humans: One Line, Big Laugh](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
- Entrypoint: `main.py` (Python 3, no dependencies)
- Output: `/output/entry.txt` — exactly one line, 141 characters
