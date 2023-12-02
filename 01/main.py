#!/usr/bin/env python
"""Day 01 of 2023 Advent of Code."""

import dataclasses
import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA = True
CALIBRATION_DOC = None

STRINGS_TO_NUMBERS = {
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
    CALIBRATION_DOC = f.read().splitlines()


@dataclasses.dataclass
class CalibrationLine:
    """A single line from the elves' calibration document. Used to find a
    calibration value.
    """

    calibration_value: int = 0
    document_line: str = None


@dataclasses.dataclass
class Calibration:
    """A calibration document made by the north pole elves to guide us on our
    mission to fix global snow production.
    """

    total_values: int = 0
    lines: list = None


def calculate_line(document_line: str) -> CalibrationLine:
    """Creates and returns a line of the calibration document, calculating
    the value for the line.

    Args:
        document_line (str): the string pulled from the calibration input.

    Returns:
        calibration_line (CalibrationLine): the calculated calibration line.
    """
    calibration_line = CalibrationLine
    calibration_line.document_line = document_line

    m = re.findall(
        r"(\d|(?:one|two|three|four|five|six|seven|eight|nine)){1}", document_line
    )

    first_digit: int = int(m[0]) if m[0].isnumeric() else STRINGS_TO_NUMBERS.get(m[0])
    last_digit: int = int(m[-1]) if m[-1].isnumeric() else STRINGS_TO_NUMBERS.get(m[-1])

    calibration_line.calibration_value = int(f"{first_digit}{last_digit}")

    return calibration_line


def ingest(document: list[str]) -> Calibration:
    """Creates and returns a calibration document.

    Args:
        document (list[str]): the raw data that will make up the calibration.

    Returns:
        Calibration: ingested calibration document that has been parsed.
    """

    calibration = Calibration

    for line in document:
        calibration_line = calculate_line(line)
        calibration.total_values += calibration_line.calibration_value

    return calibration


Calibration = ingest(CALIBRATION_DOC)
print(Calibration.total_values)
