"""Day 04 of 2023 Advent of Code."""

import os
import re

from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False  # part 1: 13, part 2: 30
CONTENTS: list[str] = []
TOTAL_SCRATCHCARDS: int = 0

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()


@dataclass
class Scratchcard:
    """A single scratchcard that contains a list of winning numbers and list of
    "numbers you have."
    """

    id: int = 0
    winning_numbers: list[int] = field(default_factory=lambda: [])
    numbers_you_have: list[int] = field(default_factory=lambda: [])
    original_card: int = 1
    duplicate_cards: int = 0

    def points_value(self) -> int:
        """Returns the total point value of this scratchcard (part 1)

        Returns:
            int: the total value of all matches on this card
        """
        counter: int = 0
        for n in self.numbers_you_have:
            if n in self.winning_numbers:
                counter = 1 if counter == 0 else counter * 2
        return counter

    def matching_numbers(self) -> int:
        """Returns how many matching numbers this scratchcard has.

        Returns:
            int: how many matching "numbers you have" this card contains
        """
        return len([n for n in self.numbers_you_have if n in self.winning_numbers])

    def total_cards(self) -> int:
        """Returns the total cards (original + duplicate) instances we have.

        Returns:
            int: the total number of this card we have
        """
        return self.original_card + self.duplicate_cards

    def add_duplicates(self, quant: int = 1) -> None:
        """Adds a duplicate card of this instance (i.e., we won another copy)."""
        self.duplicate_cards += quant


cards: list[Scratchcard] = []

for i, line in enumerate(CONTENTS):
    [card_details, card_numbers] = line.split(":")
    [winners, possessed] = card_numbers.split("|")
    card_id = re.search(r"\d+$", card_details)
    if card_id:
        cards.append(
            Scratchcard(
                id=int(card_id.group()),
                winning_numbers=[int(n) for n in winners.strip().split(" ") if n],
                numbers_you_have=[int(n) for n in possessed.strip().split(" ") if n],
            )
        )


for i, card in enumerate(cards):
    TOTAL_SCRATCHCARDS += card.total_cards()
    for j in range(1, card.matching_numbers() + 1):
        cards[i + j].add_duplicates(card.total_cards())

print(f"Part 1: {sum(c.points_value() for c in cards)}")
print(f"Part 2: {TOTAL_SCRATCHCARDS}")
