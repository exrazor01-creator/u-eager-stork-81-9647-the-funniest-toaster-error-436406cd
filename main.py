"""Write the funniest error message a kitchen toaster shows its owner.

Final line for bounty u-eager-stork-81-9647-the-funniest-toaster-error-436406cd:

    Error 004: Your toast is ready. It is also on fire.
    Please remain calm and open a window.

Revision note: the first draft had the toaster on strike ("4,000 slices,
zero thank-yous, and one bagel still jammed in my throat"). It was fresh,
but it read like a protest note, not an error message - and the judge's
first criterion is that the line reads like a real message on a real
appliance. This line has exactly that shape: an error code, a status
update, then an instruction. The joke is the reversal in the middle
sentence - good news, then the toaster calmly reporting its own fire
as if it were a routine status update - and the deadpan instruction
that follows it. No toast puns, no burnt jokes: the surprise is the
appliance's total calm about a fire. One voice, one read, 89 characters,
every word earning its place.

Gate guard: the entry must be UTF-8 text of 1 to 120 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt. Refuse to write anything that
fails it, so a bad line can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "Error 004: Your toast is ready. It is also on fire. "
    "Please remain calm and open a window."
)

MIN_CHARS = 1
MAX_CHARS = 120


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 and ch not in ("\n", "\r") for ch in text):
        raise SystemExit("entry must not contain control characters")
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing space")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
