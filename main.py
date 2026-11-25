"""One line inventing the worst superpower imaginable, for make.fun.

The power: telepathically apologising to a mosquito you have already
swallowed — and it always forgives you. The apology reaches a dead
insect that cannot hear it, cannot act on it, and forgives you anyway:
the power achieves exactly nothing, in either direction. The script
validates the line (1-140 chars, single line) and writes it to
/output/entry.txt.

Revision pass (2026-11-26): the line is now assembled from fragments by
assemble() instead of living in one constant, and validate() also
rejects control characters and requires terminal punctuation; main()
round-trips the written file against the assembled line before printing
success. Output is byte-identical to v1.
"""

from pathlib import Path

# The superpower, in fragments, assembled below (97 chars total).
_FRAGMENTS = (
    "I can telepathically apologise to any mosquito ",
    "I've already swallowed, and it always forgives me.",
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 140


def assemble() -> str:
    """Join the fragments into the single entry line."""
    return "".join(_FRAGMENTS)


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"superpower must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("superpower must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("superpower must not contain control characters")
    if text[-1] not in ".!?":
        raise ValueError("superpower must end with terminal punctuation")
    if not text:
        raise ValueError("superpower must not be only whitespace")
    return text


def main() -> None:
    text = validate(assemble())
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    if OUTPUT_FILE.read_text(encoding="utf-8") != text:
        raise ValueError("round-trip check failed: entry.txt != assembled line")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
