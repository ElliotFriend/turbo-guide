"""Day 11 of 2023 Advent of Code."""

import os
import re

from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False  # part 1: 374, part 2: something
CONTENTS: list[str] = []

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()
# print(CONTENTS)

@dataclass
class Galaxy:
    coords: tuple[int, int] = ()

    def manhattan_dist(self, other_coords: tuple[int, int]) -> int:
        # return sum(abs(a - b) for a, b in zip(self.coords, other_coords))
        return abs(self.coords[0] - other_coords[0]) + abs(self.coords[1] - other_coords[1])



@dataclass
class GalaxyImage:
    og_image: list[str] = field(default_factory=lambda: [])
    expanded_image: list[str] = field(default_factory=lambda: [])
    galaxies: list[Galaxy] = field(default_factory=lambda: [])

    def expand_universe(self) -> None:
        # first do the rows
        for _, row in enumerate(self.og_image):
            self.expanded_image.append(row)
            if not '#' in row:
                self.expanded_image.append(row)

        # then do the cols
        empty_cols: list[int] = []
        for i, _ in enumerate(self.expanded_image[0]):
            if not '#' in self.col(i):
                empty_cols.append(i)

        empty_cols.sort(reverse=True)
        for n in empty_cols:
            self.insert_empty_col(n)

    def discover_galaxies(self) -> None:
        for i, row in enumerate(self.expanded_image):
            if '#' in row:
                for gal in re.finditer(r'#', row):
                    self.galaxies.append(Galaxy((i, gal.start())))

    def row(self, index: int) -> str:
        return self.expanded_image[index] if self.expanded_image else self.og_image[index]

    def col(self, index: int) -> str:
        image_to_use = self.expanded_image if self.expanded_image else self.og_image
        return_list: list[str] = []
        for i, row in enumerate(image_to_use):
            return_list.append(image_to_use[i][index])

        return ''.join(return_list)

    def insert_empty_col(self, index: int) -> None:
        for i, row in enumerate(self.expanded_image):
            self.expanded_image[i] = f"{row[:index]}.{row[index:]}"

    def __post_init__(self) -> None:
        self.expand_universe()
        self.discover_galaxies()


gi = GalaxyImage(CONTENTS)
total_sums: int = 0

for g in gi.galaxies:
    for h in gi.galaxies:
        m_dist = g.manhattan_dist(h.coords)
        total_sums += m_dist
        # print(f"g={g.coords} h={h.coords} m_dist={m_dist}")
# print(sum([g.manhattan_dist((h.coords[0], h.coords[1]) for h in gi.galaxies) for g in gi.galaxies]))
print(f"Part 1: {total_sums // 2}")
# 9957702
