#!/usr/bin/env python
"""Day 01 of 2023 Advent of Code."""

import os
import re

from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False
CONTENTS: list[str] = []

STRINGS_TO_NUMBERS: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()


@dataclass
class CalibrationLine:
    """A single line from the elves' calibration document. Used to find a
    calibration value.
    """

    document_line: str = ""
    calibration_value: int = 0

    def __post_init__(self) -> None:
        m: list[str] = re.findall(
            r"(\d|(?:one|two|three|four|five|six|seven|eight|nine)){1}",
            self.document_line,
        )

        first_digit: int | None = (
            int(m[0]) if m[0].isnumeric() else STRINGS_TO_NUMBERS.get(m[0])
        )
        last_digit: int | None = (
            int(m[-1]) if m[-1].isnumeric() else STRINGS_TO_NUMBERS.get(m[-1])
        )

        if first_digit is not None and last_digit is not None:
            self.calibration_value = int(f"{first_digit}{last_digit}")


@dataclass
class Calibration:
    """A calibration document made by the north pole elves to guide us on our
    mission to fix global snow production.
    """

    lines: list[CalibrationLine] = field(default_factory=lambda: [])

    def total_values(self) -> int:
        """Calculates and returns the sum of all calibration values in the list
        of calibration lines.

        Returns:
            int: the sum total of all calibration values
        """
        return sum(cl.calibration_value for cl in self.lines)


calibration = Calibration([CalibrationLine(line) for line in CONTENTS])
print(calibration.total_values())
