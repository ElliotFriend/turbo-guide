"""Day 06 of 2023 Advent of Code."""

import os

from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False  # part 1: 288, part 2: 71503
CONTENTS: list[str] = []
WINNING_STRATS_PRODUCT: int = 1

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()


@dataclass
class BoatRace:
    """A single boat race from the sheet of race records given to you by an elf."""

    duration: int = 0
    best_distance: int = 0

    def calculate_button_press(self, min_bound: bool = True, iterator: int = 1) -> int:
        """Calculate and return the longest or shortest amount of time the boat
        button could be pressed and still beat the record.

        Args:
            min_bound (boolean, optional): True if clalculating minimum
                boundary, False for maximum boundary. Defaults to True.
            iterator (int, optional): Whether to increase or decrease the
                terator. Defaults to 1.

        Returns:
            int: the relevant min/max time the boat button could be pressed
        """
        button_press: int = 1 if min_bound else self.duration
        while True:
            dist_traveled = (self.duration - button_press) * button_press
            if dist_traveled > self.best_distance:
                if min_bound:
                    return button_press
                return button_press + 1
            button_press += iterator

    def count_winning_strategies(self) -> int:
        """Calculates and returns the number of strategies that could beat the
        all-time record in this boat race.

        Returns:
            int: The number of ways you could beat the record in this race.
        """
        return (
            self.calculate_button_press(min_bound=False, iterator=-1)
            - self.calculate_button_press()
        )


@dataclass
class RaceSheet:
    """A sheet containing one or more race records."""

    races: list[BoatRace] = field(default_factory=lambda: [])


race_details = zip(
    map(int, CONTENTS[0].split()[1:]),
    map(int, CONTENTS[1].split()[1:]),
)

big_race = (
    int("".join(CONTENTS[0].split()[1:])),
    int("".join(CONTENTS[1].split()[1:])),
)

part1_race_sheet = RaceSheet(
    [BoatRace(duration=t, best_distance=d) for t, d in race_details]
)
for r in part1_race_sheet.races:
    # r.run_simulations()
    WINNING_STRATS_PRODUCT *= r.count_winning_strategies()

print(f"Part 1: {WINNING_STRATS_PRODUCT}")
# 2756160


part2_race_sheet = RaceSheet(
    [BoatRace(duration=big_race[0], best_distance=big_race[1])]
)
print(f"Part 2: {part2_race_sheet.races[0].count_winning_strategies()}")
# 34788142
