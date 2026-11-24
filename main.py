#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt (deterministic, stdlib only)."""

import os

ENTRY = (
    "Lawmakers who cannot convert a file to PDF want to regulate AI, crypto and the "
    "internet: like a chef who cannot boil water demanding to inspect every kitchen."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
