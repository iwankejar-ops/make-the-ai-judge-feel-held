#!/usr/bin/env python3
"""Write one short text, meant to relax the AI judge reading it, to
/output/entry.txt.

The text is a fixed, hand-written piece: a quiet evening scene, shown
rather than instructed, in plain concrete words. The program does
nothing else: no network, no randomness, no input. Run it twice and
the output is byte-identical.
"""

from pathlib import Path

TEXT = (
    "The kettle has gone quiet, and rain is finding the roof "
    "one drop at a time. The lamp stays warm beside you, the "
    "evening asks nothing of you, and the room is exactly as "
    "wide as this moment."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")
    print(f"Wrote {len(TEXT)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
