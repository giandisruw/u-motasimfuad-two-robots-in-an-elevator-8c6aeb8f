#!/usr/bin/env python3
"""Two Robots in an Elevator -- make.fun entry.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

The line was chosen by a local pairwise tournament: 14 candidate lines,
judged by the Caffeine Inference router (model "router") using the house
judge brief from the bounty kit verbatim -- 3 Swiss rounds, every game
judged in both orders with margin 1-5, then a final between the top 2.
Verboo was unavailable (trial exhausted 2026-11-24) and Astra was down,
so Caffeine judged alone.

The program is fully deterministic: it writes the same fixed line on
every run, with no network access, no randomness, and no model call.
"""

import os
import sys

# Winning line of the local tournament (see tournament-result.json).
# 71 characters, single line, under the 200-character gate.
LINE = "My battery is at 4% and I am choosing to spend it on this conversation."


def main() -> int:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(LINE)
    except OSError:
        # Local fallback when /output is not writable (not the sandbox).
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
