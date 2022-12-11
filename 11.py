from __future__ import annotations
from util import load

class Monkey:

    def __init__(self, config: str):
        lines = config.splitlines()
        self.items = [int(i) for i in lines[1].split(":")[1].split(",")]
        self.expression = lines[2].split("=")[1].strip()
        self.test_val = int(lines[3].split()[-1])
        self.throw_true = int(lines[4].split()[-1])
        self.throw_false = int(lines[5].split()[-1])
        self.total_inspections = 0

    def inspect_items(self, mod: int, div_by_3: bool):
        while len(self.items) > 0:
            old = self.items.pop(0)
            new = int(eval(self.expression)) % mod
            if div_by_3:
                new = int(new/3)
            self.total_inspections += 1

            if new % self.test_val == 0:
                yield new, self.throw_true
            else:
                yield new, self.throw_false

    def add_item(self, item: int):
        self.items.append(item)


def calc_monkey_bysiness(data: str, rounds: int, div_by_3: bool) -> int:
    monkeys = []
    mod = 1
    for c in data.split("\n\n"):
        m = Monkey(c)
        monkeys.append(m)
        mod *= m.test_val

    for _ in range(rounds):
        for m in monkeys:
            for i, next in m.inspect_items(mod, div_by_3):
                monkeys[next].add_item(i)
            
    inspections = sorted([m.total_inspections for m in monkeys])
    return inspections[-1] * inspections[-2]

def solve(data: str):
    print("Part 1:", calc_monkey_bysiness(data, 20, True))
    print("Part 2:", calc_monkey_bysiness(data, 10000, False))


if __name__ == "__main__":
    solve(load(11))
