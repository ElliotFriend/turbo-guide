"""Day 02 of 2024 Advent of Code."""

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False
CONTENTS: list[str] = []

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()

def check_safe_level(report: list[int]) -> bool:
    rset = set(report)

    if len(rset) != len(report):
        return False

    for i in range(1, len(report) - 1):
        last = report[i - 1]
        this = report[i]
        next = report[i + 1]

        if not (last < this < next or last > this > next):
            return False

        if not (abs(this - last) < 4 and abs(next - this) < 4):
            return False

        if i + 2 == len(report):
            return True

## PART 1
safe_reports = 0
for line in CONTENTS:
    # safe = False

    report = [int(n) for n in line.split(' ')]

    if check_safe_level(report):
        safe_reports += 1
    # rset = set(report)

    # if len(rset) != len(report):
    #     continue

    # for i in range(1, len(report) - 1):
    #     last = report[i - 1]
    #     this = report[i]
    #     next = report[i + 1]

    #     if not (last < this < next or last > this > next):
    #         break

    #     if not (abs(this - last) < 4 and abs(next - this) < 4):
    #         break

    #     if i + 2 == len(report):
    #         safe = True
    #     else:
    #         continue

    # if safe:
    #     safe_reports += 1

print(f'part 1: {safe_reports}')
# 218 just right


# ## PART 2
safe_reports = 0
for line in CONTENTS:
    report = [int(n) for n in line.split(' ')]
    bad_levels = 0

    if check_safe_level(report):
        safe_reports += 1
    else:
        for i in range(len(report)):
            temp_report = report[:i]
            temp_report.extend(report[i+1:])
            # print(temp_report)

            if check_safe_level(temp_report):
                safe_reports += 1
                break

print(f'part 2: {safe_reports}')
# 977 too high
# 267 too low
# 313 too high
# 290 just right
