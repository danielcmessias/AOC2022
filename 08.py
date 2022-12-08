from typing import List
from util import load


Grid = List[List[int]]


def parse_grid(data: str) -> Grid:
    return [list(map(int, list(l))) for l in data.splitlines()]


def is_visible(grid: Grid, i: int, j: int) -> bool:
    if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[i]) - 1:
        return True

    visible_left = max(grid[i][:j]) < grid[i][j]
    visible_right = max(grid[i][j + 1 :]) < grid[i][j]
    visible_up = max([row[j] for row in grid[:i]]) < grid[i][j]
    visible_down = max([row[j] for row in grid[i + 1 :]]) < grid[i][j]
    return visible_left or visible_right or visible_up or visible_down


def scenic_score(grid: Grid, i: int, j: int) -> int:
    total_score = 1
    sight_lines = [
        grid[i][:j][::-1],
        grid[i][j + 1 :],
        [row[j] for row in grid[:i]][::-1],
        [row[j] for row in grid[i + 1 :]],
    ]
    for sl in sight_lines:
        sl_score = 0
        for h in sl:
            sl_score += 1
            if h >= grid[i][j]:
                break
        total_score *= sl_score
    return total_score


def solve(data: str):
    grid = parse_grid(data)
    n_visible = 0
    max_scenic_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            max_scenic_score = max(max_scenic_score, scenic_score(grid, i, j))
            if is_visible(grid, i, j):
                n_visible += 1

    print("Part 1:", n_visible)
    print("Part 2:", max_scenic_score)


if __name__ == "__main__":
    solve(load(8))
