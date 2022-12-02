from __future__ import annotations

from enum import IntEnum
from util import load
from typing import List

class Outcome(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6

    @classmethod
    def from_encoding(cls, enc: str) -> Outcome:
        """Converts an encoding to an Outcome."""
        match enc:
            case "X":
                return cls.LOSS
            case "Y":
                return cls.DRAW
            case "Z":
                return cls.WIN


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def play_versus(self, other: Shape) -> Outcome:
        """Return the outcome of a game between two shapes."""
        if self == other:
            return Outcome.DRAW
        elif self == Shape.ROCK and other == Shape.SCISSORS:
            return Outcome.WIN
        elif self == Shape.PAPER and other == Shape.ROCK:
            return Outcome.WIN
        elif self == Shape.SCISSORS and other == Shape.PAPER:
            return Outcome.WIN
        else:
            return Outcome.LOSS

    def from_outcome(self, outcome: Outcome):
        """Return the shape that would result in the given outcome."""
        if outcome == Outcome.DRAW:
            return self
        elif outcome == Outcome.WIN:
            return Shape(self.value % 3 + 1)
        elif outcome == Outcome.LOSS:
            return Shape((self.value - 2) % 3 + 1)

    @classmethod
    def from_encoding(cls, enc: str) -> Shape:
        """Return the shape corresponding to the given encoding."""
        match enc:
            case "A":
                return cls.ROCK
            case "B":
                return cls.PAPER
            case "C":
                return cls.SCISSORS
            case "X":
                return cls.ROCK
            case "Y":
                return cls.PAPER
            case "Z":
                return cls.SCISSORS


def _total_score_p1(lines: List[str]) -> int:
    rounds = []
    for line in lines:
        rounds.append([Shape.from_encoding(s) for s in line.split()])
    return sum([int(me) + me.play_versus(you) for you, me in rounds])


def _total_score_p2(lines: List[str]) -> int:
    total_score = 0
    for line in lines:
        you, outcome = line.split()
        you, outcome = Shape.from_encoding(you), Outcome.from_encoding(outcome)
        # What shape should I play to get the required outcome
        me = you.from_outcome(outcome)
        total_score += int(me) + int(outcome)
    return total_score


def solve(data):
    lines = data.splitlines()

    print(f"Part one: {_total_score_p1(lines)}")

    print(f"Part two: {_total_score_p2(lines)}")


if __name__ == "__main__":
    solve(load(2))
