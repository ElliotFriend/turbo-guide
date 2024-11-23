"""Day 06 of 2023 Advent of Code."""

import os

from dataclasses import dataclass

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = True  # part 1: 288, part 2: 71503
CONTENTS: list[str] = []
WINNING_STRATEGIES_PRODUCT: int = 1

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

    def calculate_button_press(self, min_bound: bool = True) -> int:
        """Calculate and return the longest or shortest amount of time the boat
        button could be pressed and still beat the record.

        Args:
            min_bound (boolean, optional): True if calculating minimum boundary,
                False for maximum boundary. Defaults to True.

        Returns:
            int: the relevant min/max time the boat button could be pressed
        """

        button_press: int = 0 if min_bound else self.duration
        iterator: int = 1 if min_bound else -1
        while True:
            dist_traveled = (self.duration - button_press) * button_press
            if dist_traveled > self.best_distance:
                if min_bound:
                    return button_press
                return button_press + 1
            button_press += iterator

    def count_winning_strategies(self) -> int:
        """Uses binary search to calculate and returns the number of strategies
        that could beat the all-time record in this boat race.

        Note that we only have to do this calculation for half of the range,
        since the results track along a hyperbola. We could even use the
        quadratic equation here if we wanted to. In either case, it's
        symmetrical and that saves us time!

        Returns:
            int: The number of ways you could beat the record in this race.
        """
        min_bound = 0
        max_bound = self.duration // 2

        def distance_traveled(button_press: int) -> int:
            return (self.duration - button_press) * button_press

        while min_bound + 1 < max_bound:
            midpoint = (min_bound + max_bound) // 2
            if distance_traveled(midpoint) > self.best_distance:
                max_bound = midpoint
            else:
                min_bound = midpoint

        first = min_bound + 1

        last = (
            (self.duration // 2)
            + (self.duration // 2 - first)
            + (1 if self.duration % 2 == 1 else 0)
        )

        return last - first + 1


# create a list of all race durations (even the everything-jammed-together one)
race_durations: list[int] = [int(n) for n in CONTENTS[0].split()[1:]]
race_durations.append(int("".join(str(rd) for rd in race_durations)))

# create a list of all best_distances (even the everything-jammed-together one)
best_distances: list[int] = [int(n) for n in CONTENTS[1].split()[1:]]
best_distances.append(int("".join(str(bd) for bd in best_distances)))

# zip everything together in tuples (race_duration, best_distance)
races_details = zip(
    race_durations,
    best_distances,
)

# construct a race sheet with all the races
race_sheet = [BoatRace(duration=t, best_distance=d) for t, d in races_details]

# for part 1, multiply all the possible winning strategies together (ignore the
# last race [it's the everything-jammed-together one])
for r in race_sheet[: len(race_sheet) - 1]:
    WINNING_STRATEGIES_PRODUCT *= r.count_winning_strategies()

print(f"Part 1: {WINNING_STRATEGIES_PRODUCT}")
# 2756160

# for part 2, just count all the winning strategies for the last race (it's the
# everything-jammed-together one)
print(f"Part 2: {race_sheet[-1].count_winning_strategies()}")
# 34788142
