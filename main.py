"""One-Line Office Jokes — make.fun bounty entry.

Writes a single-line joke about office life to /output/entry.txt.
Gate: UTF-8 text, 1-199 characters, one line, not only whitespace.
Standard library only; output is deterministic.
"""

from pathlib import Path

JOKE = (
    "Our printer only jams on documents marked urgent, "
    "so I now address it as 'sir' and cc its manager."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Enforce the sealed scorer's gate before writing: one line,
    # 1-199 characters, not only whitespace.
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be a single non-blank line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
