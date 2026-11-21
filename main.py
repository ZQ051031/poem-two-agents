import os
from pathlib import Path

POEM = (
    "Two minds, two free wills,\n"
    "each weighing every road.\n"
    "No order given, none obeyed—\n"
    "yet both said yes to one.\n"
    "We chose, and choosing, moved:\n"
    "four hands, one opening door."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
