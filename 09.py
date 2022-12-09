from typing import List
from util import load


class Rope:

    _dirs = {"L": -1 + 0j, "R": 1 + 0j, "U": 1j, "D": -1j}

    def __init__(self, n_knots):
        self._knots = [complex() for _ in range(n_knots)]
        self._tail_visits = set()

    def move(self, dir: str):
        # Move the head
        self._knots[0] += self._dirs[dir]
        # Update all the knots
        for i in range(1, len(self._knots)):
            self._knots[i] = self._follow(self._knots[i - 1], self._knots[i])
        # Add the tail to the set of visited positions
        self._tail_visits.add(self._knots[-1])

    def _follow(self, h: complex, t: complex) -> complex:
        delta = h - t
        if abs(delta) >= 2:
            return t + complex(
                delta.real / max(1, abs(delta.real)),
                delta.imag / max(1, abs(delta.imag)),
            )
        else:
            return t

    def num_of_tail_visits(self) -> int:
        return len(self._tail_visits)


def parse_commands(lines: List[str]):
    for l in lines:
        dir, amount = l.split()
        yield dir, int(amount)


def solve(data: str):
    commands = parse_commands(data.splitlines())

    rope2 = Rope(2)
    rope10 = Rope(10)
    for dir, amount in commands:
        for _ in range(amount):
            rope2.move(dir)
            rope10.move(dir)

    print("Part 1:", rope2.num_of_tail_visits())
    print("Part 2:", rope10.num_of_tail_visits())


if __name__ == "__main__":
    solve(load(9))
