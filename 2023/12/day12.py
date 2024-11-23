"""Day 12 of 2023 Advent of Code."""

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = True
CONTENTS: list[str] = []

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()
