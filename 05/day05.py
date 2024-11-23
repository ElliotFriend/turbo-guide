# """Day 05 of 2023 Advent of Code."""

import os

from collections import deque
from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False  # part 1: 35, part 2: 46
CONTENTS: list[str] = []

# with open(
#     os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
#     "r",
#     encoding="utf-8",
# ) as f:
#     CONTENTS = f.read().split("\n\n")


from functools import reduce

seeds, *mappings = open("05/input.txt").read().strip().split("\n\n")
seeds = list(map(int, seeds.split()[1:]))
# print(mappings)


def lookup(inputs, mapping):
    for start, length in inputs:
        while length > 0:
            for m in mapping.split("\n")[1:]:
                dst, src, len = map(int, m.split())
                delta = start - src
                if delta in range(len):
                    len = min(len - delta, length)
                    yield (dst + delta, len)
                    start += len
                    length -= len
                    break
            else:
                yield (start, length)
                break


seed_zips = [zip(seeds, [1] * len(seeds)), zip(seeds[0::2], seeds[1::2])]
# print([min(reduce(lookup, mappings, s))[0] for s in seed_zips])
print(seed_zips)

# @dataclass
# class MapEntry:
#     destination_start: int = 0
#     source_start: int = 0
#     range_length: int = 0

#     def destination_end(self) -> int:
#         return self.destination_start + self.range_length

#     def source_end(self) -> int:
#         return self.source_start + self.range_length


# @dataclass
# class SeedRange:
#     range_start: int = 0
#     range_length: int = 0

#     def range_stop(self) -> int:
#         return self.range_start + self.range_length

#     def is_in_range(self, number_to_check: int) -> bool:
#         return number_to_check in range(self.range_start, self.range_stop())


# @dataclass
# class AlmanacMap:
#     source: str = ""
#     destination: str = ""
#     entries: list[MapEntry] = field(default_factory=lambda: [])

#     def add_entry(self, entry: MapEntry):
#         self.entries.append(entry)

#     def convert_one(self, source_number: int) -> int:
#         for i, entry in enumerate(self.entries):
#             if source_number in range(
#                 entry.source_start, entry.source_start + entry.range_length
#             ):
#                 # print(f"found a match!")
#                 number_diff = source_number - entry.source_start
#                 return entry.destination_start + number_diff
#         return source_number

#     def convert_range(self, seed_range: list[tuple[int, int]]) -> list[tuple[int, int]]:
#         a_list = []
#         for i, entry in enumerate(self.entries):
#             nr_list = []
#             while seed_range:
#                 (start, end) = seed_range.pop()
#                 # print(f"start={start} end={end}")
#                 before = (start, min(end, entry.source_start))
#                 # print(f"before={before}")
#                 inter = (max(start, entry.source_start), min(entry.source_end(), end))
#                 after = (max(entry.source_end(), start), end)

#                 if before[1] > before[0]:
#                     nr_list.append(before)
#                 if inter[1] > inter[0]:
#                     a_list.append(
#                         (
#                             inter[0] - entry.source_start + entry.destination_start,
#                             inter[1] - entry.source_start + entry.destination_start,
#                         )
#                     )
#                 if after[1] > after[0]:
#                     nr_list.append(after)
#             seed_range = nr_list
#         # print(f"a_list={a_list}")
#         # print(f"seed_range={seed_range}")
#         return a_list + seed_range
#         # for (dest, src, sz) in self.tuples:
#         #     src_end = src+sz
#         #     NR = []
#         #     while R:
#         #         # [st                                     ed)
#         #         #          [src       src_end]
#         #         # [BEFORE ][INTER            ][AFTER        )
#         #         (st,ed) = R.pop()
#         #         # (src,sz) might cut (st,ed)
#         #         before = (st,min(ed,src))
#         #         inter = (max(st, src), min(src_end, ed))
#         #         after = (max(src_end, st), ed)
#         #         if before[1]>before[0]:
#         #             NR.append(before)
#         #         if inter[1]>inter[0]:
#         #             A.append((inter[0]-src+dest, inter[1]-src+dest))
#         #         if after[1]>after[0]:
#         #             NR.append(after)
#         #     R = NR
#         # return A+R


# @dataclass
# class Almanac:
#     seeds: list[int] = field(default_factory=lambda: [])
#     seed_ranges: list[SeedRange] = field(default_factory=lambda: [])
#     maps: dict[str, AlmanacMap] = field(default_factory=lambda: {})

#     def add_map(self, source_string: str, map: AlmanacMap) -> None:
#         self.maps[source_string] = map

#     def find_seed_location(self, source_num: int) -> int:
#         source: str = "seed"
#         dest_num: int = 0
#         while True:
#             dest_num = self.maps[source].convert_one(source_num)
#             dest = self.maps[source].destination or ""
#             if dest == "location":
#                 break
#             source = dest
#             source_num = dest_num
#         return dest_num

#     def find_seed_locations(self) -> dict[int, int]:
#         seed_location_dict = {}
#         for seed in self.seeds:
#             source: str = "seed"
#             source_num: int = seed
#             dest_num: int = 0
#             while True:
#                 dest_num = self.maps[source].convert_one(source_num)
#                 dest = self.maps[source].destination or ""
#                 if dest == "location":
#                     break
#                 source = dest
#                 source_num = dest_num
#             seed_location_dict[seed] = dest_num
#         return seed_location_dict

#     def find_seed_range_locations(self) -> dict[int, int]:
#         seed_location_dict = {}
#         for seed_range in self.seed_ranges:
#             source: str = "seed"
#             source_num: int = 0
#             # print(len(list(range(seed_range.range_start, seed_range.range_start + seed_range.range_length))))
#             # Am I essentially supposed to go through all the various AlmanacMaps
#             # and then calculate

#         return seed_location_dict


# elf_almanac = Almanac()

# for i, entry in enumerate(CONTENTS):
#     if i == 0:
#         # sort out the seeds first
#         seeds = [int(n) for n in entry.split()[1:]]
#         elf_almanac.seeds = seeds.copy()

#         for range_start, range_length in zip(seeds[::2], seeds[1::2]):
#             elf_almanac.seed_ranges.append(
#                 SeedRange(
#                     range_start=range_start,
#                     range_length=range_length,
#                 )
#             )

#         # while len(seeds):
#         #     [range_start, range_length] = seeds[:2]
#         #     del seeds[:2]
#         #     print(f"appending range({range_start, range_length})")
#         #     range_start = seeds.pop(0)
#         #     # print(range_start)
#         #     range_length = seeds.pop(0)
#         #     print(f"range({range_start}, {range_start+range_length})")
#         #     elf_almanac.seed_ranges.append(SeedRange(
#         #         range_start=range_start,
#         #         range_length=range_length,
#         #     ))
#     else:
#         # figure out the maps one-by-one, i guess
#         mapping_list = entry.splitlines()
#         [source_string, dest_string] = mapping_list[0].split()[0].split("-to-")
#         del mapping_list[0]
#         almanac_map = AlmanacMap(source=source_string, destination=dest_string)
#         for mapping_line in mapping_list:
#             [dest_start, source_start, length] = [int(n) for n in mapping_line.split()]
#             almanac_map.add_entry(
#                 MapEntry(
#                     destination_start=dest_start,
#                     source_start=source_start,
#                     range_length=length,
#                 )
#             )
#             elf_almanac.add_map(source_string=source_string, map=almanac_map)


# print(f"Part 1: {min([v for k, v in elf_almanac.find_seed_locations().items()])}")
# # 621354867

# # range_locations = elf_almanac.find_seed_range_locations()
# # # print(range_locations)
# # r_locations = [range_locations[k] for k in range_locations]
# # r_locations.sort()
# # print(f"Part 2: {r_locations}")

# # print([sr.is_in_range(445) for sr in elf_almanac.seed_ranges])
# part_2 = []
# for sr in elf_almanac.seed_ranges:
#     seed_range = [(sr.range_start, sr.range_stop())]
#     # print(f"seed_range={seed_range}")
#     for source_string, alm_map in elf_almanac.maps.items():
#         seed_range = alm_map.convert_range(seed_range)
#         # print(f"seed_range={seed_range}")
#     part_2.append(min(seed_range[0]))

# # closest_location = elf_almanac.find_seed_location(min(part_2))
# print(f"Part 2: {min(part_2)}")
# # print(f"Part 2b: {elf_almanac.find_seed_location(min(part_2))}")
# # 3011035656 - too high
# # 506368722 - too high still
# # 15880236

# # P2 = []
# # pairs = list(zip(seed[::2], seed[1::2]))
# # for st, sz in pairs:
# #     # inclusive on the left, exclusive on the right
# #     # e.g. [1,3) = [1,2]
# #     # length of [a,b) = b-a
# #     # [a,b) + [b,c) = [a,c)
# #     R = [(st, st+sz)]
# #     for f in Fs:
# #         R = f.apply_range(R)
# #     #print(len(R))
# #     P2.append(min(R)[0])
# # print(min(P2))
