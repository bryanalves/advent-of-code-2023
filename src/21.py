from itertools import count
from math import ceil

def parsedInput():
    lines = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
'''.rstrip('\n')

    lines = open("res/21.dat","rt").read().strip()
    lines = lines.split('\n')
    start = [(i, line.index('S')) for i, line in enumerate(lines) if 'S' in line]
    return tuple(lines), start[0]

def move(grid, pos, seen, gardens, remaining):
    if not remaining:
        if grid[pos[0]][pos[1]] in ['.', 'S']:
            gardens.add(pos)
        return

    dirs = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    ]

    for d in dirs:
        newpos = (pos[0] + d[0], pos[1] + d[1])
        gridpos = grid[newpos[0] % len(grid)][newpos[1] % len(grid)]
        if gridpos in '.S' and (newpos, remaining) not in seen:
            seen.add((newpos, remaining))
            move(grid, newpos, seen, gardens, remaining - 1)

def part1():
    grid, start = parsedInput()

    remaining = 64
    seen = set()
    seen.add((start, remaining))
    gardens = set()

    move(grid, start, seen, gardens, remaining)
    return len(gardens)

def part2():
    grid, start = parsedInput()
    done = []
    todo = set([start])
    gardens = {(x, y)
        for x, r in enumerate(grid)
        for y, c in enumerate(r) if c in '.S'
    }
    dirs = [ (-1, 0), (1, 0), (0, 1), (0, -1) ]

    gridsize = len(grid)
    target = 26501365

    for s in count():
        if s % gridsize == gridsize // 2:
            done.append(len(todo))

        if len(done) == 3:
            break

        todo = {
            (t[0] + d[0], t[1] + d[1])
            for t in todo
            for d in dirs
            if ((t[0] + d[0]) % gridsize, (t[1] + d[1]) % gridsize) in gardens
        }

    def solve(seen_states, ceiling):
        m = seen_states[1] - seen_states[0]
        n = seen_states[2] - seen_states[1]
        a = (n - m) // 2
        b = m - 3 * a
        c = seen_states[0] - b - a

        return a * ceiling**2 + b * ceiling + c

    return solve(done, ceil(target / gridsize))

if __name__ == '__main__':
    print(part1())
    print(part2())
