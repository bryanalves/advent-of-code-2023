import sys
import functools
from frozendict import frozendict

sys.setrecursionlimit(100000)

def parsedInput():
    lines = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
'''.rstrip('\n')

    lines = open("res/23.dat","rt").read().strip()
    lines = lines.split('\n')
    start = lines[0].index('.')
    target = lines[-1].index('.')

    grid = {}
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            grid[y, x] = ch

    return (0, start), (len(lines) - 1, target), frozendict(grid)

def neighbor(pos, tile):
    adj = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0),
    }

    y, x = pos
    ay, ax =  adj[tile]

    return (y + ay, x + ax)

def take_a_slippery_step(grid, pos, end, path, steps):
    if pos == end:
      return steps

    longest = -1

    for i, dir in enumerate('v>^<'):
        move = neighbor(pos, dir)
        tile = grid.get(move, '#')
        if tile == '#':
            continue
        if move in path:
            continue
        if tile == '^<v>'[i]:
            continue

        new_path = set(path)
        new_path.add(move)
        new_steps = take_a_slippery_step(grid, move, end, new_path, steps + 1)
        longest = max(longest, new_steps)
    return longest

@functools.cache
def take_a_step(grid, pos, end, path, steps):
    if pos == end:
      return steps

    longest = -1

    for _, dir in enumerate('v>^<'):
        move = neighbor(pos, dir)
        tile = grid.get(move, '#')
        if tile == '#':
            continue
        if move in path:
            continue
        # if tile == '^<v>'[i]:
        #     continue

        new_path = set(path)
        new_path.add(move)
        new_steps = take_a_step(grid, move, end, frozenset(new_path), steps + 1)
        longest = max(longest, new_steps)
    return longest

def part1():
    start, end, grid = parsedInput()
    path = set()
    path.add(start)
    longest_walk = take_a_slippery_step(grid, start, end, path, 0)
    return longest_walk

def part2():
    start, end, grid = parsedInput()
    path = set()
    path.add(start)
    longest_walk = take_a_step(grid, start, end, frozenset(path), 0)
    return longest_walk

if __name__ == '__main__':
    print(part1())
    # print(part2())
