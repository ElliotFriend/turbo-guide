"""Day 08 of 2023 Advent of Code."""

import math
import os

from dataclasses import dataclass
from itertools import cycle
from multiprocessing import Pool

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False  # part 1: 2, part 2: 6
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

map_dict: dict[str, dict[str, str]] = dict()

for node_map in list(CONTENTS[2:]):
    # print(node_map.split())
    node_name, _, left_node, right_node = node_map.split()
    # print(node_name)
    map_dict[node_name] = {
        "L": left_node.replace("(", "").replace(",", ""),
        "R": right_node.replace(")", ""),
    }


def take_step(current_node: str, direction: str) -> str:
    return map_dict[current_node][direction]


current_node = START_NODE
step_count: int = 0

while current_node != END_NODE:
    current_node = take_step(current_node, next(left_right_steps))
    step_count += 1

print(f"Part 1: {step_count}")
# 11911

step_counts: list[int] = []

for node in list(n for n, _ in map_dict.items() if n.endswith("A")):
    current_node = node
    step_count = 0
    while not current_node.endswith("Z"):
        step_count += 1
        current_node = take_step(current_node, next(left_right_steps))
    step_counts.append(step_count)

lcm = 1
for count in step_counts:
    lcm *= count // math.gcd(lcm, count)

print(f"Part 2: {lcm}")
# 10151663816849
