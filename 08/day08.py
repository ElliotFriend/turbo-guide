"""Day 08 of 2023 Advent of Code."""

import os

from dataclasses import dataclass
from itertools import cycle

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False  # part 1: 2?, part 2: something
CONTENTS: list[str] = []
START_NODE: str = "AAA"
END_NODE: str = "ZZZ"

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()

left_right_steps = cycle(list(CONTENTS[0]))
# print(next(left_right_steps))

# @dataclass
# class NetworkNodeMap:

map_dict = dict()

for node_map in list(CONTENTS[2:]):
    # print(node_map.split())
    node_name, _, left_node, right_node = node_map.split()
    # print(node_name)
    map_dict[node_name] = {'L': left_node.replace("(", "").replace(",", ""), "R": right_node.replace(")", "")}

# print(map_dict)

current_node = START_NODE
step_count: int = 0

while current_node != END_NODE:
    current_node = map_dict[current_node][next(left_right_steps)]
    step_count += 1

print(f"Part 1: {step_count}")
# 11911
