"""Day 04 of 2024 Advent of Code."""

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

## PART 1
xmas_count = 0
for y in range(len(CONTENTS)):
    row = CONTENTS[y]
    for x in range(len(row)):
        if row[x] == "X":
            if row[x:x+4] == "XMAS":
                # 3 of these - GOOD
                xmas_count += 1
            if row[x-3:x+1] == "SAMX":
                # 2 of these - GOOD
                xmas_count += 1

            col = ''.join([a[x] for a in CONTENTS])
            if col[y:y+4] == "XMAS":
                # 1 of these (i think) - GOOD
                xmas_count += 1
            if col[y-3:y+1] == "SAMX":
                # 2 of these (i think) - GOOD
                xmas_count += 1

            # check top-left to bottom-right diagonal
            if (
                x + 3 < len(CONTENTS[y]) and
                y + 3 < len(row) and
                CONTENTS[y+1][x+1] == "M" and
                CONTENTS[y+2][x+2] == "A" and
                CONTENTS[y+3][x+3] == "S"
            ):
                # 1 of these - GOOD
                xmas_count += 1
            if (
                x - 3 >= 0 and
                y - 3 >= 0 and
                CONTENTS[y-1][x-1] == "M" and
                CONTENTS[y-2][x-2] == "A" and
                CONTENTS[y-3][x-3] == "S"
            ):
                # 4 of these (i think) - GOOD
                xmas_count += 1

            # check bottom-left to top-right diagonal
            if (
                x - 3 >= 0 and
                y + 3 < len(row) and
                CONTENTS[y+1][x-1] == "M" and
                CONTENTS[y+2][x-2] == "A" and
                CONTENTS[y+3][x-3] == "S"
            ):
                # 1 of these - GOOD
                xmas_count += 1
            if (
                x + 3 < len(CONTENTS[y]) and
                y - 3 >= 0 and
                CONTENTS[y-1][x+1] == "M" and
                CONTENTS[y-2][x+2] == "A" and
                CONTENTS[y-3][x+3] == "S"
            ):
                # 4 of these - GOOD
                xmas_count += 1

            # print(f"({x}, {y}) - {col}")
        # check if it's 'X'
        # check left-to-right
        # check right-to-left
        # check down
        # check up



print(f"part 1: {xmas_count}")
# 2363 too low
# 2373 too low
# 2378 just right

## PART 2
x_mas_count = 0
for y in range(len(CONTENTS)):
    row = CONTENTS[y]
    for x in range(len(row)):
        if row[x] == "A":
            if (
                (
                    y - 1 >= 0 and x - 1 >= 0 and
                    y + 1 < len(row) and x + 1 < len(CONTENTS[y])
                ) and ((
                    (
                        CONTENTS[y+1][x+1] == "M" and
                        CONTENTS[y-1][x-1] == "S"
                    ) or (
                        CONTENTS[y+1][x+1] == "S" and
                        CONTENTS[y-1][x-1] == "M"
                    )
                ) and (
                    (
                        CONTENTS[y-1][x+1] == "M" and
                        CONTENTS[y+1][x-1] == "S"
                    ) or (
                        CONTENTS[y-1][x+1] == "S" and
                        CONTENTS[y+1][x-1] == "M"
                    )
                ))
            ):
                x_mas_count += 1

print(f"part 2: {x_mas_count}")
# 1796 just right
