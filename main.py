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
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
