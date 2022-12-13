import math
from util import load

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dijkstra(grid, start, end):
    Q = set()
    dist = {}
    prev = {}
    for n in [(i, j) for i in range(len(grid)) for j in range(len(grid[i]))]:
        dist[n] = math.inf
        prev[n] = None
        Q.add(n)
    
    dist[start] = 0
    while len(Q) > 0:
        u = min(Q, key=lambda x: dist[x])
        Q.remove(u)
        for d in DIRS:
            v = (u[0] + d[0], u[1] + d[1])
            if v[0] < 0 or v[1] < 0 or v[0] >= len(grid) or v[1] >= len(grid[0]):
                continue
            delta = ord(grid[u[0]][u[1]]) - ord(grid[v[0]][v[1]]) 
            if delta > 1:
                continue
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    
    return dist


def solve(data: str):
    grid = [list(l) for l in data.splitlines()]
    start, end = None, None
    trail_starts = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)
            elif grid[i][j] == "a":
                trail_starts.append((i, j))

    grid[start[0]][start[1]] = "a"
    grid[end[0]][end[1]] = "z"
    
    distances = dijkstra(grid, end, start)
    print("Part 1:", distances[start])
    print("Part 2:", min([distances[t] for t in trail_starts]))

            
if __name__ == "__main__":
    solve(load(12))
