from typing import List, Tuple
from util import load

Stacks = List[List[str]]
Commands = List[Tuple[int, int, int]]


def parse_stacks(lines: List[str]) -> Tuple[Stacks, List[str]]:
    stacks = [[] for _ in range((len(lines[0]) // 4) + 1)]
    for lineNumber, line in enumerate(lines):
        for i, j in enumerate(range(1, len(lines[0]), 4)):
            c = line[j]
            if c.isdigit():
                # Also return the remaining lines to parse the commands from
                return (stacks, lines[lineNumber + 2 :])
            if c != " ":
                stacks[i].append(c)


def parse_cmds(lines: List[str]) -> Commands:
    for l in lines:
        _, amount, _, origin, _, target = l.split()
        yield int(amount), int(origin) - 1, int(target) - 1


def part1(stacks: Stacks, commands: Commands) -> str:
    _stacks = [s.copy() for s in stacks]
    for amount, origin, target in commands:
        for _ in range(amount):
            _stacks[target].insert(0, _stacks[origin].pop(0))
    return "".join([s[0] for s in _stacks])


def part2(stacks: Stacks, commands: Commands) -> str:
    _stacks = [s.copy() for s in stacks]
    for amount, origin, target in commands:
        segment = _stacks[origin][:amount]
        _stacks[origin] = _stacks[origin][amount:]
        _stacks[target] = segment + _stacks[target]
    return "".join([s[0] for s in _stacks])


def solve(data: str):
    lines = data.splitlines()
    stacks, lines = parse_stacks(lines)
    commands = parse_cmds(lines)

    print("Part 1:", part1(stacks, commands))
    print("Part 2:", part2(stacks, commands))


if __name__ == "__main__":
    solve(load(5))
