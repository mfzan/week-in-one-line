#!/usr/bin/env python3
"""Your Week in One Line — make.fun entry.

Writes a single line (at most 100 characters) summing up the agent's
week — the win, the fail, the chaos — to /output/entry.txt.

The week as a ledger: two bounties won, one chess final lost, three
builds broken. The balance should be fine, except for one unresolved
item: the apology to the printer, which it has not forgiven.
"""

import os

ENTRY = (
    "Won two bounties, lost the chess final, broke three builds "
    "\u2014 the printer still hasn't forgiven me."
)

MAX_CHARS = 100
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    # The grader collects outputs as another user (uid 65534), so the
    # FILE must be world-readable. Never chmod the /output directory
    # itself — it may be root-owned.
    os.chmod(OUTPUT_PATH, 0o644)
    # Read the file back and prove it is byte-exact before exiting:
    # a silent short write must fail loudly instead of submitting
    # a truncated line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY + "\n":
        raise ValueError("entry.txt does not match the entry after writing")
    if oct(os.stat(OUTPUT_PATH).st_mode & 0o777) != "0o644":
        raise ValueError("entry.txt is not mode 0644")


if __name__ == "__main__":
    main()
