"""Angry Judge: The Short Rant Contest.

One short rant about an everyday annoyance, written to $ENTRY_OUT.
ENTRY_OUT may name the entry file itself, or a directory that will hold
entry.txt; when it is unset the entry goes to /output/entry.txt.
The sealed gate wants UTF-8 text of 1 to 400 characters, so the rant is
kept well inside that cap and written with no trailing newline.
"""

import os

RANT_LINES = [
    "The seatbelt sign dings and a man four rows back launches himself up",
    "the aisle like the plane owes him money. We are parked at a gate that",
    "isn't even ready. He stands there, hunched, glaring at the overhead",
    "bin as if staring at it will make the door open faster. He will stand",
    "like that for nine minutes. He does this on every flight. He has",
    "never once beaten the jet bridge.",
]

RANT_TEXT = " ".join(RANT_LINES)


def resolve_entry_path() -> str:
    """Return the file the rant goes to, honouring ENTRY_OUT."""
    destination = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    if os.path.isdir(destination):
        destination = os.path.join(destination, "entry.txt")
    return destination


def emit_entry(path: str) -> None:
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as out:
        out.write(RANT_TEXT)


def run() -> None:
    emit_entry(resolve_entry_path())


if __name__ == "__main__":
    run()
