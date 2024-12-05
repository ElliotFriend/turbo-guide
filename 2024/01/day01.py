"""Day 01 of 2024 Advent of Code."""

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

# print(CONTENTS)

left_list = []
right_list = []
# print(left_list)
# print(right_list)

for numbers in CONTENTS:
    # print(numbers)
    # print(numbers.split('   '))
    [left, right] = numbers.split('   ')
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()
# print(left_list[0])
# print(right_list[0])

## PART 1
i = 0
total = 0
while i < len(left_list):
    distance = right_list[i] - left_list[i]
    # distance = 0
    # if right_list[i] > left_list[i]:
    #     distance = right_list[i] - left_list[i]
    # else:
    #     distance = left_list[i] - right_list[i]
    total += abs(distance)
    i += 1

print(f'part 1: {total}')
# 877009 too low
# 1590491 correct

## PART 2
sim_score = 0
for lnum in left_list:
    count = right_list.count(lnum)
    sim_score += lnum * count

print(f'part 2: {sim_score}')
