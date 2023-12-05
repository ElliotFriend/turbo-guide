"""Day 03 of 2023 Advent of Code."""

import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False
CONTENTS: list[str] = []
PART_NUMBERS_SUM: int = 0
GEAR_RATIOS_SUM: int = 0

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()


for i, line in enumerate(CONTENTS):
    digit_matches_iter = re.finditer(r"\d+", line)
    for digit_match in digit_matches_iter:
        if digit_match.group():
            start = 0 if digit_match.start() == 0 else digit_match.start() - 1
            end = len(line) if digit_match.end() == len(line) else digit_match.end() + 1
            symbol_match_prev = (
                [] if i == 0 else re.findall(r"[^\d\.]", CONTENTS[i - 1][start:end])
            )
            symbol_match_curr = re.findall(r"[^\d\.]", line[start:end])
            symbol_match_next = (
                []
                if i == len(CONTENTS) - 1
                else re.findall(r"[^\d\.]", CONTENTS[i + 1][start:end])
            )
            if symbol_match_prev or symbol_match_curr or symbol_match_next:
                PART_NUMBERS_SUM += int(digit_match.group())

    star_matches_iter = re.finditer(r"\*", line)
    for star_match in star_matches_iter:
        if star_match.group():
            adjacent_parts = []
            coords = (star_match.start(), i)

            # check the previous line
            if i > 0:
                adjacent_matches_iter_prev = re.finditer(r"\d+", CONTENTS[i - 1])
                for adjacent_match_prev in adjacent_matches_iter_prev:
                    if (
                        coords[0] >= adjacent_match_prev.start() - 1
                        and coords[0] <= adjacent_match_prev.end()
                    ):
                        adjacent_parts.append(int(adjacent_match_prev.group()))

            # check same line
            adjacent_match_curr_left = re.search(r"\d+$", line[: coords[0]])
            if adjacent_match_curr_left:
                adjacent_parts.append(int(adjacent_match_curr_left.group()))
            adjacent_match_curr_right = re.search(r"^\d+", line[coords[0] + 1 :])
            if adjacent_match_curr_right:
                adjacent_parts.append(int(adjacent_match_curr_right.group()))

            # check the next line
            if i < len(CONTENTS):
                adjacent_matches_iter_next = re.finditer(r"\d+", CONTENTS[i + 1])
                for adjacent_match_next in adjacent_matches_iter_next:
                    if (
                        coords[0] >= adjacent_match_next.start() - 1
                        and coords[0] <= adjacent_match_next.end()
                    ):
                        adjacent_parts.append(int(adjacent_match_next.group()))

            if len(adjacent_parts) == 2:
                GEAR_RATIOS_SUM += adjacent_parts[0] * adjacent_parts[1]

print(f"Part 1: {PART_NUMBERS_SUM}")
# 533775
print(f"Part 2: {GEAR_RATIOS_SUM}")
# 78236071
