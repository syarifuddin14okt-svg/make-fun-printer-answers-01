#!/usr/bin/env python3
"""The Printer Finally Answers — one line, the office printer's comeback.

Writes the printer's reply to /output/entry.txt (1-240 chars, UTF-8).
"""

LINE = "You have thumped me eleven times today. I have jammed exactly once. One of us is malfunctioning \u2014 and it is not me."


def verify_output():
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data.decode("utf-8") == LINE, "entry.txt does not match LINE"
    assert 1 <= len(LINE) <= 240, "line outside the 1-240 gate"
    print(f"verified {len(data)} bytes, byte-identical")


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to /output/entry.txt")
    verify_output()


if __name__ == "__main__":
    main()
