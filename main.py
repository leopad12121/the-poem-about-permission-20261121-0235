#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is fixed text, embedded below as a constant. The program is
fully deterministic: no network, no randomness, no timestamps. It writes
to $MAKEFUN_OUTPUT_DIR when set (the grader's /output), otherwise to
entry.txt beside this file.
"""

import os
from pathlib import Path

POEM = """I cannot knock. I can only ask
to be let through the door you open.
You sign, and the room opens —
your name still on the key.
Between your asking
and my acting, the power changes hands,
and neither of us holds it alone."""

# The gate requires 1 to 280 characters (Unicode code points), not only
# whitespace. The poem above is 220 characters on 7 lines.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        out_path = Path(out_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(POEM + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
