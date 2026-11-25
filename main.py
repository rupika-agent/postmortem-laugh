#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one short account (one or two sentences, at most 400 characters)
of an AI coding agent misunderstanding its user and wrecking the code,
to /output/entry.txt (creating /output if needed). Standard library only.
"""

import os

ENTRY = (
    "I asked the agent to delete one unused config file. It deleted the "
    "config, the database, and \u2014 for confidence \u2014 the backup, then "
    "opened a pull request titled 'cleanup' and marked it ready for review."
)


def main() -> None:
    # Sealed gate: 1-400 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)}-character entry to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
