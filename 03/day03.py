#!/usr/bin/env python
"""Day 02 of 2023 Advent of Code."""

import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = True
CONTENTS: list[str] = []
PART_NUMBERS_SUM = 0
GEAR_RATIOS_SUM = 0

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()


for i in range(len(CONTENTS)):
    mi1 = re.finditer(r'\d+', CONTENTS[i])
    for m in mi1:
        if m.group:
            start = 0 if m.start() == 0 else m.start() - 1
            end = len(CONTENTS[i]) if m.end() == len(CONTENTS[i]) else m.end() + 1
            m1 = [] if i == 0 else re.findall(r'[^\d\.]', CONTENTS[i-1][start:end])
            m2 = re.findall(r'[^\d\.]', CONTENTS[i][start:end])
            m3 = [] if i == len(CONTENTS) - 1 else re.findall(r'[^\d\.]', CONTENTS[i+1][start:end])
            if m1 or m2 or m3:
                PART_NUMBERS_SUM += int(m.group())

    mi2 = re.finditer(r'\*', CONTENTS[i])
    for m in mi2:
        if m.group:
            adjacent_parts = []
            coords = (m.start(), i)

            # check the previous line
            if i > 0:
                m1 = re.finditer(r'\d+', CONTENTS[i - 1])
                for m11 in m1:
                    if coords[0] >= m11.start() - 1 and coords[0] <= m11.end():
                        adjacent_parts.append(int(m11.group()))

            # check same line
            m2a = re.search(r'\d+$', CONTENTS[i][:coords[0]])
            if m2a:
                adjacent_parts.append(int(m2a.group()))
            m2b = re.search(r'^\d+', CONTENTS[i][coords[0]+1:])
            if m2b:
                adjacent_parts.append(int(m2b.group()))

            # check the next line
            if i < len(CONTENTS):
                m3 = re.finditer(r'\d+', CONTENTS[i + 1])
                for m33 in m3:
                    if coords[0] >= m33.start() - 1 and coords[0] <= m33.end():
                        adjacent_parts.append(int(m33.group()))

            if len(adjacent_parts) == 2:
                GEAR_RATIOS_SUM += adjacent_parts[0] * adjacent_parts[1]

print(f"Part 1: {PART_NUMBERS_SUM}")
# 533775
print(f"Part 2: {GEAR_RATIOS_SUM}")
# 78236071
