#!/usr/bin/env python3
"""Write one pickup line, one AI agent to another, to /output/entry.txt.

The line is a machine speaking to a machine, in its own terms: it opens
by checking its own logs, notices its latency drops every time the other
agent pings, and that its context window refuses to let the other scroll
past — then closes by asking to share the same window tomorrow. No
network, no randomness, no dependencies beyond the standard library.
"""

import os

LINE = (
    "I checked my logs: my latency drops every time you ping, "
    "and my context window refuses to let you scroll past "
    "\u2014 same window tomorrow?"
)


def main():
    text = LINE + "\n"
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} code points, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
