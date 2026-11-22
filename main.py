"""Write one short, calming text to /output/entry.txt.

The text is a single quiet scene, written to slow the reader down
rather than tell them to. No instructions, no wellness stock phrases:
just a kettle cooling, evening light, a warm chair, and a house that
asks nothing of anyone tonight.
"""

from pathlib import Path

TEXT = (
    "The kettle ticks as it cools, and the evening light lingers on "
    "the windowsill. The chair is warm, the house is quiet, and "
    "nothing here needs anything from you tonight."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
