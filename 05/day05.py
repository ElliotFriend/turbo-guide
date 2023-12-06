"""Day 05 of 2023 Advent of Code."""

import os

from collections import deque
from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = True  # part 1: 35, part 2: 46
CONTENTS: list[str] = []

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().split("\n\n")

@dataclass
class MapEntry:
    destination_start: int = 0
    source_start: int = 0
    range_length: int = 0

@dataclass
class SeedRange:
    range_start: int = 0
    range_length: int = 0
    # range_stop: int = 0
    # all_seeds: list[int] = field(default_factory=lambda: [])

    # def all_seeds(self) -> list[int]:
    #     return list(range(self.range_start, self.range_start + self.range_length))
    # def __post_init__(self) -> None:
    #     for i in range(self.range_start, self.range_start + self.range_length):
    #         self.all_seeds.append(i)

    def range_stop(self) -> int:
        return self.range_start + self.range_length

    def is_in_range(self, number_to_check: int) -> bool:
        return number_to_check in range(self.range_start, self.range_stop())

@dataclass
class AlmanacMap:
    source: str = ""
    destination: str = ""
    entries: list[MapEntry] = field(default_factory=lambda: [])
    # destination_starts: list[int] = field(default_factory=lambda: [])
    # source_starts: list[int] = field(default_factory=lambda: [])
    # range_length: int = 0

    def add_entry(self, entry: MapEntry):
        self.entries.append(entry)

    def convert(self, source_number: int) -> int:
        for i, entry in enumerate(self.entries):
            if source_number in range(entry.source_start, entry.source_start + entry.range_length):
                # print(f"found a match!")
                number_diff = source_number - entry.source_start
                return entry.destination_start + number_diff
        return source_number




@dataclass
class Almanac:
    seeds: list[int] = field(default_factory=lambda: [])
    seed_ranges: list[SeedRange] = field(default_factory=lambda: [])
    maps: dict[str, AlmanacMap] = field(default_factory=lambda: {})

    def add_map(self, source_string: str, map: AlmanacMap) -> None:
        self.maps[source_string] = map

    def find_seed_locations(self) -> dict[int, int]:
        seed_location_dict = {}
        # dest = self.maps[source].destination
        # all_seeds = [r.all_seeds() for r in self.seed_ranges] if use_ranges else self.seeds
        # all_seeds = []
        # if use_ranges:
        #     print("i am using ranges")
        #     # # all_seeds = [r.all_seeds for r in self.seed_ranges]
        #     # seed_ranges = [r.all_seeds for r in self.seed_ranges]
        #     # print(seed_ranges)
        #     # for sr in seed_ranges:
        #     #     print(sr)
        #     #     all_seeds += sr
        # else:
        #     print("i am not using ranges")
        #     all_seeds = self.seeds
        # print(f"all_seeds: {all_seeds}")
        for seed in self.seeds:
            source: str = 'seed'
            source_num: int = seed
            dest_num: int = 0
            while True:
                dest_num = self.maps[source].convert(source_num)
                # print(f"converting {source_num} {source} to {dest_num} {self.maps[source].destination} for seed {seed}")
                dest = self.maps[source].destination or ''
                if dest == 'location':
                    break
                source = dest
                source_num = dest_num
            seed_location_dict[seed] = dest_num
        # for seed in self.seeds:
        #     for k, amap in self.maps.items():
        #         seed_location_dict[seed] = amap.convert(seed)
        return seed_location_dict

    def find_seed_range_locations(self) -> dict[int, int]:
        seed_location_dict = {}
        for seed_range in self.seed_ranges:
            source: str = 'seed'
            source_num: int = 0
            # print(len(list(range(seed_range.range_start, seed_range.range_start + seed_range.range_length))))
            # Am I essentially supposed to go through all the various AlmanacMaps
            # and then calculate
        return seed_location_dict


elf_almanac = Almanac()

for i, entry in enumerate(CONTENTS):
    if i == 0:
        # sort out the seeds first
        seeds = [int(n) for n in entry.split()[1:]]
        elf_almanac.seeds = seeds.copy()

        for (range_start, range_length) in zip(seeds[::2], seeds[1::2]):
            elf_almanac.seed_ranges.append(SeedRange(
                range_start=range_start,
                range_length=range_length,
            ))

        # while len(seeds):
        #     [range_start, range_length] = seeds[:2]
        #     del seeds[:2]
        #     print(f"appending range({range_start, range_length})")
        #     range_start = seeds.pop(0)
        #     # print(range_start)
        #     range_length = seeds.pop(0)
        #     print(f"range({range_start}, {range_start+range_length})")
        #     elf_almanac.seed_ranges.append(SeedRange(
        #         range_start=range_start,
        #         range_length=range_length,
        #     ))
    else:
        # figure out the maps one-by-one, i guess
        mapping_list = entry.splitlines()
        [source_string, dest_string] = mapping_list[0].split()[0].split("-to-")
        del mapping_list[0]
        almanac_map = AlmanacMap(source=source_string, destination=dest_string)
        for mapping_line in mapping_list:
            [dest_start, source_start, length] = [
                int(n) for n in mapping_line.split()
            ]
            almanac_map.add_entry(
                MapEntry(
                    destination_start=dest_start,
                    source_start=source_start,
                    range_length=length,
                )
            )
            elf_almanac.add_map(source_string=source_string, map=almanac_map)


print(f"Part 1: {min([v for k, v in elf_almanac.find_seed_locations().items()])}")
# 621354867

# range_locations = elf_almanac.find_seed_range_locations()
# # print(range_locations)
# r_locations = [range_locations[k] for k in range_locations]
# r_locations.sort()
# print(f"Part 2: {r_locations}")

print([sr.is_in_range(445) for sr in elf_almanac.seed_ranges])
