#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes a single one-line joke about office life to entry.txt.
Deterministic: the same bytes on every run. Standard library only.
"""

import argparse
import os
import sys

JOKE = (
    "I asked my calendar for focus time, so it booked a meeting "
    'called "Focus Time" with twelve people and no agenda.'
)


def resolve_output_path(cli_output):
    """Return the entry.txt path, honouring --output, then
    $MAKEFUN_OUTPUT_DIR, then the default /output/entry.txt."""
    target = cli_output or os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if target.endswith(".txt"):
        return target
    return os.path.join(target, "entry.txt")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the office joke entry to entry.txt."
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output file or directory (default: $MAKEFUN_OUTPUT_DIR or /output).",
    )
    args = parser.parse_args(argv)

    path = resolve_output_path(args.output)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
