from typing import List
from util import load


def parse_commands(lines: List[str]) -> List[List[str, int, int]]:
    cmds = []
    for l in lines:
        parts = l.split()
        if parts[0] == "addx":
            cmds.append([parts[0], int(parts[1]), 2])
        else:
            cmds.append([parts[0], None, 1])
    return cmds


def solve(data: str):
    commands = parse_commands(data.splitlines())

    pixels = []
    register = 1
    cycle = 1
    sum_cycles = 0
    cmd = None
    while commands:
        if cycle == 20 or (cycle - 20) % 40 == 0:
            sum_cycles += register * (cycle)

        if register - 1 <= (cycle - 1) % 40 <= register + 1:
            pixels.append("#")
        else:
            pixels.append(".")

        if not cmd:
            cmd = commands.pop(0)
        if cmd[0] == "addx":
            cmd[2] -= 1
            if cmd[2] == 0:
                register += cmd[1]
                cmd = None
        else:
            cmd = None
        cycle += 1

    print("Part 1:", sum_cycles)
    print("Part 2:")
    for i in range(0, len(pixels), 40):
        print("".join(pixels[i : i + 40]))


if __name__ == "__main__":
    solve(load(10))
