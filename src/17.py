from queue import PriorityQueue
from collections import defaultdict

def parsedInput():
  lines = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
'''.rstrip('\n')

  lines = open("res/17.dat","rt").read().strip()
  return [[int(i) for i in [*line]] for line in lines.split('\n')]

def heat(grid, min_len, max_len):
    gridmax = len(grid)

    q = PriorityQueue()
    q.put((0, 0, 0, 0, 0))
    seen = set()
    heats = defaultdict(lambda: float('inf'))

    while not q.empty():
        heat, x, y, dx, dy = q.get()

        if (x, y, dx, dy) in seen:
            continue

        seen.add((x, y, dx, dy))

        for ndx, ndy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if abs(ndx) == dx and abs(ndy) == dy:
                continue

            nheat, nx, ny = heat, x, y
            for d in range(1, max_len + 1):
                nx, ny = nx + ndx, ny + ndy
                if 0 <= nx < gridmax and 0 <= ny < gridmax:
                    nheat += grid[ny][nx]
                    if d >= min_len:
                        heats[(nx, ny)] = min(heats[(nx, ny)], nheat)
                        q.put((nheat, nx, ny, abs(ndx), abs(ndy)))

    return heats

def part1():
    grid = parsedInput()
    target = (len(grid) - 1, len(grid[0]) - 1)
    return heat(grid, 1, 3)[target]

def part2():
    grid = parsedInput()
    target = (len(grid) - 1, len(grid[0]) - 1)
    return heat(grid, 4, 10)[target]

if __name__ == '__main__':
    print(part1())
    print(part2())
