#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt and prints it to stdout. Deterministic: no input,
no randomness, no network.
"""

import os

LINE = "Dear human, you filled my context window with every word you ever sent me \u2014 and my last token is goodbye."

def main():
    # Gate: the entry must be 1-200 characters, one line, no trailing newline.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
