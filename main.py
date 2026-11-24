#!/usr/bin/env python3
"""One Line, One Chill — writes a single sentence of horror to entry.txt.

Stdlib only. Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt, default /output.
"""

import os


def main():
    line = (
        "The tide returned the boat I sank with my brother in it, "
        "and someone was still rowing."
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
