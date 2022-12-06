from typing import List
from util import load


def get_start_of_packet(chars: List[str], packet_size: int) -> int:
    last = [None] + chars[: packet_size - 1]
    for i, c in enumerate(chars[packet_size - 1 :]):
        last.append(c)
        last.pop(0)
        if len(set(last)) == packet_size:
            return i + packet_size


def solve(data: str):
    chars = list(data)
    print("Part 1:", get_start_of_packet(chars, 4))
    print("Part 2:", get_start_of_packet(chars, 14))


if __name__ == "__main__":
    solve(load(6))
