#!/usr/bin/env python

import os, re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA = True

calibration_doc = None
with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'), "r"
) as f:
    calibration_doc = f.read().splitlines()


def word_to_int(number_word: str | int) -> int:
    match number_word:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9


class Calibration:
    def __init__(self, document):
        self.total_values: int = 0
        self.lines = []

        for line in document:
            c_line = CalibrationLine(line)
            self.total_values += c_line.calibration_value


class CalibrationLine:
    def __init__(self, document_line: str):
        self.calibration_value: int = 0

        m = re.findall(
            r"(\d|(?:one|two|three|four|five|six|seven|eight|nine)){1}", document_line
        )
        self.first_digit: int = int(m[0]) if m[0].isnumeric() else word_to_int(m[0])
        self.last_digit: int = int(m[-1]) if m[-1].isnumeric() else word_to_int(m[-1])

        self.calibration_value = int(f"{self.first_digit}{self.last_digit}")


calibration = Calibration(calibration_doc)
print(calibration.total_values)
