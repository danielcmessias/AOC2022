from typing import List
from util import load


def _get_totals(lines: List[str]) -> List[int]:
    count = 0
    totals = []
    for l in lines:
        if l == "":
            totals.append(count)
            count = 0
        else:
            count += int(l)
    return totals


def solve(data):
    totals = sorted(_get_totals(data.splitlines()))

    # Part 1
    print(f"Part one: {totals[-1]}")

    # Part 2
    print(f"Part two: {sum(totals[-3:])}")


if __name__ == "__main__":
    solve(load(1))
