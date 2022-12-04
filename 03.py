from typing import List

from util import load


def score_char(char: str) -> int:
    if char.isupper():
        return ord(char) - ord("A") + 27
    else:
        return ord(char) - ord("a") + 1


def part1(lines: List[str]) -> int:
    total_score = 0
    for line in lines:
        chars = list(line)
        r1 = set(chars[: len(chars) // 2])
        r2 = set(chars[len(chars) // 2 :])
        total_score += score_char(min(r1.intersection(r2)))
    return total_score


def part2(lines: List[str]) -> int:
    total_score = 0
    for i in range(0, len(lines), 3):
        r1, r2, r3 = [set(r) for r in lines[i : i + 3]]
        total_score += score_char(min(r1.intersection(r2).intersection(r3)))
    return total_score


def solve(data: str):
    lines = data.splitlines()
    print("Part 1", part1(lines))
    print("Part 2", part2(lines))


if __name__ == "__main__":
    solve(load(3))
