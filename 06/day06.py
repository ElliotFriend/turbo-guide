"""Day 06 of 2023 Advent of Code."""

import os

from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = True  # part 1: 288, part 2: 71503
CONTENTS: list[str] = []
WINNING_STRATS_PRODUCT: int = 1

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()

@dataclass
class RaceStrategy:
    race_time: int = 0
    charge_time: int = 0
    distance_traveled: int = 0

    def simulate(self) -> int:
        """Simulates how the race goes following this strategy.

        Returns:
            int: the distance traveled by the boat during the race
        """
        speed = self.charge_time
        remaining_time = self.race_time - self.charge_time
        self.distance_traveled = speed * remaining_time
        return self.distance_traveled


@dataclass
class BoatRace:
    duration: int = 0
    best_distance: int = 0
    winning_strategies: list[RaceStrategy] = field(default_factory=lambda: [])

    def run_simulations(self):
        for i in range(self.duration + 1):
            strat = RaceStrategy(race_time=self.duration, charge_time=i)
            if strat.simulate() > self.best_distance:
                self.winning_strategies.append(strat)

    def count_winning_strategies(self) -> int:
        return len(self.winning_strategies)

@dataclass
class RaceSheet:
    races: list[BoatRace] = field(default_factory=lambda: [])

race_details = zip(
    map(int, CONTENTS[0].split()[1:]),
    map(int, CONTENTS[1].split()[1:]),
)

big_race = (
    int(''.join(CONTENTS[0].split()[1:])),
    int(''.join(CONTENTS[1].split()[1:])),
)
print(big_race)

part1_race_sheet = RaceSheet([BoatRace(duration=t, best_distance=d) for t, d in race_details])
for r in part1_race_sheet.races:
    r.run_simulations()
    WINNING_STRATS_PRODUCT *= r.count_winning_strategies()

print(f"Part 1: {WINNING_STRATS_PRODUCT}")
# 2756160


part2_race_sheet = RaceSheet([BoatRace(duration=big_race[0], best_distance=big_race[1])])
part2_race_sheet.races[0].run_simulations()
print(f"Part 2: {part2_race_sheet.races[0].count_winning_strategies()}")
# 34788142
