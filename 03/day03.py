"""Day 03 of 2023 Advent of Code."""

import os
import re

from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = True  # part 1: 4361, part 2: 467835
CONTENTS: list[str] = []
PART_NUMBERS_SUM: int = 0
GEAR_RATIOS_SUM: int = 0
RE_SYMBOL_DIGIT_SYMBOL: re.Pattern = r"([^\d\.])?(\d+)([^\d\.])?"
RE_NON_DIGIT_SYMBOL: re.Pattern = r"[^\d\.]"

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()


@dataclass
class PartNumber:
    """A single part number in the gondola engine schematic."""

    pn_value: int = 0
    pn_row: int = 0
    pn_x_start: int = 0
    pn_x_end: int = 0

    def __repr__(self) -> str:
        return f"PartNumber: {self.pn_value}"


@dataclass
class Gear:
    """A single gear in the gondola engine schematic."""

    gear_x: int = 0
    gear_y: int = 0
    adjacent_part_numbers: list[int] = field(default_factory=lambda: [])

    def is_valid_gear(self) -> bool:
        """Tells whether the gear is a valid gear in the schematic (that is, it
        is adjacent to exactly two part numbers).

        Returns:
            bool: true if the gear is valid, false if it is not
        """
        return len(self.adjacent_part_numbers) == 2

    def gear_ratio(self) -> int:
        """Calculates and returns the gear ratio of a valid gear (returns 0 if
        it is an invalid gear).

        Returns:
            int: the calculated gear ratio
        """
        return (
            self.adjacent_part_numbers[0] * self.adjacent_part_numbers[1]
            if self.is_valid_gear()
            else 0
        )


@dataclass
class EngineSchematic:
    """The entire schematic for the gondola engine."""

    og_contents: list[str] = field(default_factory=lambda: [])
    part_numbers: list[PartNumber] = field(default_factory=lambda: [])
    gears: list[Gear] = field(default_factory=lambda: [])

    def __post_init__(self) -> None:
        for i, line in enumerate(self.og_contents):
            # we'll need to know upper- and lower-bounds for both searches
            top: int = 0 if i == 0 else i - 1
            bottom: int = (
                len(self.og_contents) - 1 if i == len(self.og_contents) - 1 else i + 1
            )

            # First, find all the valid parts and add them to the list
            digit_matches_iter = re.finditer(r"\d+", line)
            for digit_match in digit_matches_iter:
                # set the bounding box coords (vert, horiz)
                left: int = 0 if digit_match.start() == 0 else digit_match.start() - 1
                right: int = (
                    len(self.og_contents[i]) - 1
                    if digit_match.end() == len(self.og_contents[i]) - 1
                    else digit_match.end() + 1
                )

                # now, make a string including all surrounding characters
                context_string: str = ""
                for j in range(top, bottom + 1):
                    context_string += self.og_contents[j][left:right]

                # if there's a non-digit, non-period symbol anywhere in that
                # string, it's a valid part number
                if re.search(RE_NON_DIGIT_SYMBOL, context_string):
                    self.part_numbers.append(
                        PartNumber(
                            pn_value=int(digit_match.group()),
                            pn_row=i,
                            pn_x_start=digit_match.start(),
                            pn_x_end=digit_match.end(),
                        )
                    )

            gear_matches_iter = re.finditer(r"\*", line)
            for gear_match in gear_matches_iter:
                pass

    def part_numbers_sum(self) -> int:
        """Adds and returns the part numbers of all valid schematic parts.

        Returns:
            int: the total sum of all valid parts in the engine schematic
        """
        return sum([p.pn_value for p in self.part_numbers])

    def sum_gear_ratios(self) -> int:
        """Adds and returns the gear ratios of all valid schematic gears.

        Returns:
            int: the total sum of all valid gear ratios in the engine schematic
        """
        return sum([g.gear_ratio() for g in self.gears])


eng_sch: EngineSchematic = EngineSchematic(og_contents=CONTENTS)

# for i, line in enumerate(CONTENTS):
#     digit_matches_iter = re.finditer(r"\d+", line)
#     for digit_match in digit_matches_iter:
#         if digit_match.group():
#             start = 0 if digit_match.start() == 0 else digit_match.start() - 1
#             end = len(line) if digit_match.end() == len(line) else digit_match.end() + 1
#             symbol_match_prev = (
#                 [] if i == 0 else re.findall(r"[^\d\.]", CONTENTS[i - 1][start:end])
#             )
#             symbol_match_curr = re.findall(r"[^\d\.]", line[start:end])
#             symbol_match_next = (
#                 []
#                 if i == len(CONTENTS) - 1
#                 else re.findall(r"[^\d\.]", CONTENTS[i + 1][start:end])
#             )
#             if symbol_match_prev or symbol_match_curr or symbol_match_next:
#                 PART_NUMBERS_SUM += int(digit_match.group())

#     star_matches_iter = re.finditer(r"\*", line)
#     for star_match in star_matches_iter:
#         adjacent_parts = []
#         coords = (star_match.start(), i)

#         # check the previous line
#         if i > 0:
#             adjacent_matches_iter_prev = re.finditer(r"\d+", CONTENTS[i - 1])
#             for adjacent_match_prev in adjacent_matches_iter_prev:
#                 if (
#                     coords[0] >= adjacent_match_prev.start() - 1
#                     and coords[0] <= adjacent_match_prev.end()
#                 ):
#                     adjacent_parts.append(int(adjacent_match_prev.group()))

#         # check same line
#         adjacent_match_curr_left = re.search(r"\d+$", line[: coords[0]])
#         if adjacent_match_curr_left:
#             adjacent_parts.append(int(adjacent_match_curr_left.group()))
#         adjacent_match_curr_right = re.search(r"^\d+", line[coords[0] + 1 :])
#         if adjacent_match_curr_right:
#             adjacent_parts.append(int(adjacent_match_curr_right.group()))

#         # check the next line
#         if i < len(CONTENTS):
#             adjacent_matches_iter_next = re.finditer(r"\d+", CONTENTS[i + 1])
#             for adjacent_match_next in adjacent_matches_iter_next:
#                 if (
#                     coords[0] >= adjacent_match_next.start() - 1
#                     and coords[0] <= adjacent_match_next.end()
#                 ):
#                     adjacent_parts.append(int(adjacent_match_next.group()))

#         if len(adjacent_parts) == 2:
#             GEAR_RATIOS_SUM += adjacent_parts[0] * adjacent_parts[1]

print(f"Part 1: {eng_sch.part_numbers_sum()}")
# 533775
print(f"Part 2: {GEAR_RATIOS_SUM}")
# 78236071
