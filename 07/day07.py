"""Day 07 of 2023 Advent of Code."""

import os

from dataclasses import dataclass, field
from operator import methodcaller

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False  # part 1: 6440, part 2: 5905
CONTENTS: list[str] = []
CARD_STRENGTHS: list[str] = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "J",
    "Q",
    "K",
    "A",
]
CARD_STRENGTHS_DICT: dict[str, int] = {k: v for v, k in enumerate(CARD_STRENGTHS)}
CARD_STRENGTHS_JOKER: list[str] = [
    "J",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "Q",
    "K",
    "A",
]
CARD_STRENGTHS_JOKER_DICT: dict[str, int] = {
    k: v for v, k in enumerate(CARD_STRENGTHS_JOKER)
}
HAND_STRENGTHS: list[str] = [
    "high_card",
    "one_pair",
    "two_pair",
    "three_kind",
    "full_house",
    "four_kind",
    "five_kind",
]
HAND_STRENGTHS_DICT: dict[str, int] = {k: v for v, k in enumerate(HAND_STRENGTHS)}

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()


@dataclass
class CamelCardsHand:
    hand: list[str] = field(default_factory=lambda: [])
    bid: int = 0
    jokers: bool = False

    numeric_hand: list[int] = field(default_factory=lambda: [])
    hand_type: str = ""
    hand_rank: int = 0

    def __post_init__(self) -> None:
        self.numeric_hand = (
            [CARD_STRENGTHS_JOKER_DICT[c] for c in hand]
            if self.jokers
            else [CARD_STRENGTHS_DICT[c] for c in hand]
        )
        hand_dict = {i: self.hand.count(i) for i in self.hand}
        num_jokers: int = (
            (hand_dict["J"] if "J" in hand_dict else 0) if self.jokers else 0
        )
        # print(f"num_jokers={num_jokers} hand_dict={hand_dict}")
        for c in sorted(hand_dict, key=hand_dict.get, reverse=True):
            card_count = hand_dict[c]
            # if c == 'J':
            #     continue
            if self.jokers:
                if c == "J" and len(hand_dict) > 1:
                    continue
                if not self.hand_type and card_count < 5 and c != "J":
                    card_count += num_jokers
            match card_count:
                case 5:
                    self.hand_type = "five_kind"
                case 4:
                    self.hand_type = "four_kind"
                case 3:
                    self.hand_type = "three_kind"
                case 2:
                    if self.hand_type == "three_kind":
                        self.hand_type = "full_house"
                    elif self.hand_type == "one_pair":
                        self.hand_type = "two_pair"
                    else:
                        self.hand_type = "one_pair"
                case _:
                    if not self.hand_type:
                        self.hand_type = "high_card"

    def __eq__(self, other) -> bool:
        return self.numeric_hand == other.numeric_hand

    def __lt__(self, other) -> bool:
        return self.numeric_hand < other.numeric_hand

    def hand_strength(self) -> int:
        return HAND_STRENGTHS_DICT[self.hand_type]


@dataclass
class CamelCardsList:
    hands_list: list[CamelCardsHand] = field(default_factory=lambda: [])

    def calculate_winnings(self) -> int:
        return sum([h.bid * h.hand_rank for h in self.hands_list])

    def order_by_card_strength(self) -> None:
        self.hands_list.sort()

    def order_by_hand_type(self) -> None:
        self.hands_list.sort(key=methodcaller("hand_strength"))

    def assign_real_rankings(self) -> None:
        for i, hand in enumerate(self.hands_list):
            hand.hand_rank = i + 1

    def __post_init__(self) -> None:
        self.order_by_card_strength()
        self.order_by_hand_type()
        self.assign_real_rankings()


camel_cards_list = []

for i, hand_and_bid in enumerate(CONTENTS):
    [hand, bid] = hand_and_bid.split()
    camel_cards_list.append(CamelCardsHand(hand=list(hand), bid=int(bid)))

camel_cards_list = CamelCardsList(camel_cards_list)

print(f"Part 1: {camel_cards_list.calculate_winnings()}")
# 250058342

camel_cards_list = []

for i, hand_and_bid in enumerate(CONTENTS):
    [hand, bid] = hand_and_bid.split()
    camel_cards_list.append(
        CamelCardsHand(
            hand=list(hand),
            bid=int(bid),
            jokers=True,
        )
    )

camel_cards_list = CamelCardsList(camel_cards_list)

print(f"Part 2: {camel_cards_list.calculate_winnings()}")
# 250506580
