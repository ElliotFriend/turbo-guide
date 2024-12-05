"""Day 03 of 2024 Advent of Code."""

import os, re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False
CONTENTS: list[str] = []

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()

def mul(mul_args: tuple[str]) -> int:
    return int(mul_args[0]) * int(mul_args[1])

def add_muls(corrupt_memory: str) -> int:
    total = 0
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", corrupt_memory)
    for m in matches:
        total += mul(m)
    return total

## PART 1
NEW_CONTENTS = CONTENTS[:1] if SAMPLE_DATA else CONTENTS
# print(f"new {''.join(NEW_CONTENTS)}")
running_total = add_muls(''.join(NEW_CONTENTS))
# for line in NEW_CONTENTS:
#     running_total += add_muls(line)

print(f'part 1: {running_total}')
# 178794710 just right

## PART 2
NEW_CONTENTS = CONTENTS[1:] if SAMPLE_DATA else CONTENTS
running_total = 0
# for line in CONTENTS[1:]:
# for line in NEW_CONTENTS:
line = ''.join(NEW_CONTENTS)
segments = re.split(r"don't\(\)", line)
enabled = segments.pop(0)
running_total += add_muls(enabled)

for s in segments:
    splits = re.split(r"do\(\)", s)
    if len(splits) > 1:
        running_total += add_muls(''.join(splits[1:]))

print(f'part 2: {running_total}')
# 68374313 too low
# 89846869 too high
# 76729637 just right
