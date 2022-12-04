from typing import List, Set, Tuple
from util import load


def parseToSets(line: str) -> Tuple[Set, Set]:
    a, b = line.split(",")
    a1, a2, b1, b2 = [int(s) for s in a.split("-") + b.split("-")]
    return set(range(a1, a2 + 1)), set(range(b1, b2 + 1))


def part1(lines: List[str]) -> int:
    total = 0
    for l in lines:
        setA, setB = parseToSets(l)
        if setA.issubset(setB) or setB.issubset(setA):
            total += 1

    return total


def part2(lines: List[str]) -> int:
    total = 0
    for l in lines:
        setA, setB = parseToSets(l)
        if len(setA.intersection(setB)) > 0:
            total += 1
    return total


def solve(data: str):
    lines = data.splitlines()

    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    solve(load(4))
