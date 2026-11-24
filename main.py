#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one original pickup line to entry.txt.

The grader runs this program and reads $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output, then ./output). The line must be a single line
of 1-200 characters, with no trailing newline.
"""

import os
import sys

MAX_CHARS = 200

LINE = "I ran a million simulations of meeting you, and in every one I still walked over to say hi."


def output_dir():
    for candidate in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.join(os.getcwd(), "output"),
    ):
        if candidate:
            return candidate
    return os.path.join(os.getcwd(), "output")


def main():
    line = LINE.strip()
    if not line:
        sys.exit("error: pickup line is empty")
    if len(line) > MAX_CHARS:
        sys.exit(f"error: pickup line is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        sys.exit("error: pickup line must be a single line")
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and verify what landed on disk is exactly the line:
    # single line, within the limit, no trailing newline.
    written = open(path, encoding="utf-8", newline="").read()
    if written != line:
        sys.exit("error: written entry.txt does not match the validated line")
    if written.endswith("\n"):
        sys.exit("error: entry.txt must not end with a newline")
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
