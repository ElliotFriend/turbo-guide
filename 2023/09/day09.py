"""Day 09 of 2023 Advent of Code."""

import os

from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False  # part 1: 114, part 2: 2
CONTENTS: list[str] = []

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()


@dataclass
class OasisValueHistory:
    """A record of historical data for this particular oasis data value."""

    values_history: list[int] = field(default_factory=lambda: [])
    future_predicted_value: int = 0
    past_predicted_value: int = 0

    def make_predictions(self) -> None:
        """Extrapolate the predicted past and future values for the oasis data
        in question. When calculations are done, store the values for later.
        """

        def make_difference_list(starting_list: list[int]) -> list[int]:
            return list(
                starting_list[i + 1] - val
                for i, val in enumerate(starting_list)
                if i < len(starting_list) - 1
            )

        diff_lists: list[list[int]] = [self.values_history] + [
            make_difference_list(self.values_history)
        ]
        while not all(d == 0 for d in diff_lists[-1]):
            diff_lists.append(make_difference_list(diff_lists[-1]))

        diff_lists.reverse()
        for i, diff_list in enumerate(diff_lists):
            if i < len(diff_lists) - 1:
                diff_lists[i + 1].append(diff_list[-1] + diff_lists[i + 1][-1])
                diff_lists[i + 1].insert(0, diff_lists[i + 1][0] - diff_list[0])
        self.future_predicted_value = diff_lists[-1][-1]
        self.past_predicted_value = diff_lists[-1][0]

    def __post_init__(self) -> None:
        self.make_predictions()


oasis_history: list[OasisValueHistory] = []

for values_history in CONTENTS:
    ovh = OasisValueHistory(list(map(int, values_history.split())))
    oasis_history.append(ovh)


print(f"Part 1: {sum(list(vh.future_predicted_value for vh in oasis_history))}")
# 1887980197

print(f"Part 2: {sum(list(vh.past_predicted_value for vh in oasis_history))}")
# 990
