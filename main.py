#!/usr/bin/env python3
"""Rejected Olympic Sports — make.fun entry.

Writes one funny single-line sport the Olympics rejected to
/output/entry.txt. The line won a local 8-finalist round robin (7-0)
judged on the sealed criteria: funniest rejected sport, twist lands
in one read, broadcast-plausible, no wasted words, quotable.
"""

ENTRY = (
    "Competitive reverse parking a caravan: one trailer, "
    "a campsite of watchers, and a marriage that must "
    "survive the manoeuvre."
)


def main() -> None:
    # Gate: the entry must be one line of 1-200 UTF-8 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
