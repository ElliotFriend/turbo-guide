"""Day 10 of 2023 Advent of Code."""

import os

# import numpy as np
from collections import defaultdict

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = True  # part 1: 4 and then 8, part 2: 4 and then 8 and then 10
CONTENTS: list[str] = []
STEP_COUNT: int = 0
CURR_POS: tuple[int, int] = (0, 0)
CURR_PIPE: str = ""
CAME_FROM: str = ""
VALID_MOVES = {
    "|": ["n", "s"],
    "-": ["e", "w"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
}
CAME_FROM_DICT = {
    "n": "s",
    "e": "w",
    "s": "n",
    "w": "e",
}
VISITED_COORDS: dict[int, list[tuple[int, int]]] = defaultdict(list)
# VISITED_COORDS: list[int, tuple[int, int]] = []
CONTAINED_AREA: int = 0


with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()


def move_direction(
    current_position: tuple[int, int], direction: str
) -> tuple[int, int]:
    match direction:
        case "n":
            return (current_position[0] - 1, current_position[1])
        case "e":
            return (current_position[0], current_position[1] + 1)
        case "s":
            return (current_position[0] + 1, current_position[1])
        case "w":
            return (current_position[0], current_position[1] - 1)


for i, y in enumerate(CONTENTS):
    for j, x in enumerate(y):
        if x == "S":
            CURR_POS = (i, j)
            break
    else:
        continue
    break


def find_adjacent_characters(current_position: tuple[int, int]) -> dict[str, str]:
    adjacent_chars: dict[str, str] = {}
    for direction in ["n", "e", "s", "w"]:
        adjacent_coords = move_direction(current_position, direction)
        adjacent_chars[direction] = CONTENTS[adjacent_coords[0]][adjacent_coords[1]]
    return adjacent_chars


def find_valid_options(current_position: tuple[int, int]) -> list[str]:
    all_options = find_adjacent_characters(current_position)
    valid_options: list[str] = []
    for k, v in all_options.items():
        while len(valid_options) < 2:
            if v != ".":
                match k:
                    case "n":
                        if v == "|" or v == "F" or v == "7" or v == "S":
                            valid_options.append(k)
                    case "e":
                        if v == "-" or v == "7" or v == "J" or v == "S":
                            valid_options.append(k)
                    case "s":
                        if v == "|" or v == "J" or v == "L" or v == "S":
                            valid_options.append(k)
                    case "w":
                        if v == "-" or v == "L" or v == "F" or v == "S":
                            valid_options.append(k)
    return valid_options


# print(f"Found S!! (x={START_COL}, y={START_ROW})")
# print(f"See? Here it is: {CONTENTS[START_ROW][START_COL]}")
# print(f"x={j} y={i}")

# while CURR_PIPE != "S":
while True:
    if CURR_PIPE == "S":
        break
    elif CURR_PIPE == "":
        valid_options = ["e", "s"] if SAMPLE_DATA else ["n", "e"]
    else:
        valid_options = VALID_MOVES[CURR_PIPE].copy()

    VISITED_COORDS[CURR_POS[0]].append(CURR_POS)
    if CAME_FROM in valid_options:
        valid_options.remove(CAME_FROM)
    step = valid_options[0]
    CURR_POS = move_direction(CURR_POS, step)
    STEP_COUNT += 1
    CAME_FROM = CAME_FROM_DICT[step]
    CURR_PIPE = CONTENTS[CURR_POS[0]][CURR_POS[1]]

print(f"Part 1: {STEP_COUNT // 2}")
# 6947

# VISITED_COORDS = sorted(VISITED_COORDS, key=lambda coord: (coord[0], coord[1]))
# VISITED_COORDS_DICT = {coord[0]:coord for _, coord in enumerate(VISITED_COORDS)}
for k, v in VISITED_COORDS.items():
    VISITED_COORDS[k] = sorted(v)
    print(f"CONTAINED_AREA={CONTAINED_AREA} VISITED_COORDS[{k}]={VISITED_COORDS[k]}")
    # too_subtract_coord = VISITED_COORDS[k][0]
    on_near_side: bool = True
    for i, coord in enumerate(VISITED_COORDS[k]):
        if i < len(VISITED_COORDS[k]) - 1:
            if abs(VISITED_COORDS[k][i + 1][1] - coord[1]) != 1 and on_near_side:
                far_side = VISITED_COORDS[k][i + 1]
                near_side = VISITED_COORDS[k][i]
                print(f"near_side={near_side} far_side={far_side}")
                CONTAINED_AREA += far_side[1] - near_side[1] - 1
            on_near_side = not on_near_side
    # coord_pairs = zip(VISITED_COORDS[k][::2], VISITED_COORDS[k][1::2])
    # for pair in coord_pairs:
    #     # print(pair)
    #     print(pair)
    #     CONTAINED_AREA += pair[1][1] - pair[0][1] - 1
    # for coord in VISITED_COORDS[k][::2]:
    #     print(coord)
# print(VISITED_COORDS)

# for i, coord in enumerate(VISITED_COORDS):
#     # # first coord is "S"
#     # if VISITED_COORDS[i + 1][0] == coord[0]:
#     #     # next coord is on the same line, so add the distance?

#     pass

print(f"Part 2: {CONTAINED_AREA}")
# 390 - too high
