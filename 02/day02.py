"""Day 02 of 2023 Advent of Code."""

import os
import re

from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE_DATA: bool = False
CONTENTS: list[str] = []

STARTING_DICT: dict[str, int] = {
    "red": 0,
    "green": 0,
    "blue": 0,
}

with open(
    os.path.join(__location__, f'{"sample" if SAMPLE_DATA else "input"}.txt'),
    "r",
    encoding="utf-8",
) as f:
    CONTENTS = f.read().splitlines()


@dataclass
class GameRound:
    """A single round of the game, where the elf removes a selection of cubes
    from the bag and reveals them to you.
    """

    round_record: str = ""
    # pylint: disable=unnecessary-lambda
    shown_cubes: dict[str, int] = field(default_factory=lambda: STARTING_DICT.copy())

    def __post_init__(self) -> None:
        m: list[str] = re.findall(r"(\d+) (red|green|blue)", self.round_record)
        for sc in m:
            self.shown_cubes[sc[1]] = int(sc[0])


@dataclass
class Game:
    """A record of the game which was played. Including how many of each color
    cube was revealed in each round, the game id, whether it was possible under
    the part 1 conditions, and the cube set power for the part 2 conditions.
    """

    game_record: str = ""
    id: int = 0
    rounds: list[GameRound] = field(default_factory=lambda: [])
    possible: bool = True
    # pylint: disable=unnecessary-lambda
    cubes_required: dict[str, int] = field(default_factory=lambda: STARTING_DICT.copy())

    def __post_init__(self) -> None:
        [game_string, rounds_string] = self.game_record.split(": ")
        m = re.search(r"^Game (\d{1,3})$", game_string)
        if m:
            self.id = int(m.groups()[0])

        for r in rounds_string.split("; "):
            game_round = GameRound(r)
            bag_contains: dict[str, int] = {
                "red": 12,
                "green": 13,
                "blue": 14,
            }

            for cube_color, cube_number in game_round.shown_cubes.items():
                if cube_number > bag_contains.get(cube_color, 0):
                    self.possible = False

                if cube_number > self.cubes_required.get(cube_color, 0):
                    self.cubes_required[cube_color] = cube_number

            self.rounds.append(game_round)

    def cube_set_power(self) -> int:
        """Calculates the cube set power for the given game: The product of the
        fewest possible cubes of each color to make each round feasible.

        Returns:
            int: the cube set power for the fewest cubes possible in this game
        """
        i = 1
        for col in self.cubes_required:
            i *= self.cubes_required.get(col, 1)
        return i


games = [Game(line) for line in CONTENTS]

# PART 1: What is the sum of IDs of all possible games?
print(f"Part 1: {sum(g.id for g in games if g.possible)}")

# PART 2: What is the sum of all cube set powers of _ALL_ games?
print(f"Part 2: {sum(g.cube_set_power() for g in games)}")
