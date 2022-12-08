"""
This solution is a bit gross, should have just used Pathlib. Oh well...
"""

from collections import defaultdict
from functools import reduce
from operator import getitem
from typing import List
from util import load


def get_in_dict(d: dict, keys: List):
    return reduce(getitem, keys, d)


def set_in_dict(d: dict, keys: List, value):
    get_in_dict(d, keys[:-1])[keys[-1]] = value


def cd(cmd, currentPath) -> List[str]:
    if cmd == "/":
        return ["/"]
    elif cmd == "..":
        return currentPath[:-1]
    else:
        return currentPath + [cmd]


def _make_tree():
    return defaultdict(_make_tree)


def parse_tree(lines: List[str]):
    tree = _make_tree()
    currentPath = ["/"]
    for l in lines:
        args = l.split()
        if l.startswith("$"):
            cmd = args[1]
            if cmd == "cd":
                currentPath = cd(args[2], currentPath)
        else:
            # ls
            dirPath = currentPath + [args[1]]
            if args[0] == "dir":
                get_in_dict(tree, dirPath)
            else:
                set_in_dict(tree, dirPath, args[0])

    return tree


def sum_dir(tree, path=[], all_dirs=[]):
    total = 0
    l = []
    for k, v in tree.items():
        if isinstance(v, dict):
            vTotal, vDirs = sum_dir(v, path + [k], all_dirs)
            l.extend(vDirs)
            total += vTotal
        else:
            total += int(v)

    return total, l + [("/".join(path), total)]


def solve(data: str):
    tree = parse_tree(data.splitlines())

    used_space, all_dirs = sum_dir(tree)
    print("Part 1:", sum([s[1] for s in all_dirs if s[1] <= 100000]))

    min_delete_size = 30000000 - (70000000 - used_space)
    viable_dirs = sorted(
        [d for d in all_dirs if d[1] >= min_delete_size], key=lambda x: x[1]
    )
    print("Part 2:", viable_dirs[0][1])


if __name__ == "__main__":
    solve(load(7))
