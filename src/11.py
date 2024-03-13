from pprint import pprint
from itertools import combinations
from bisect import bisect

def parsedInput():
  lines = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''.rstrip('\n')

  lines = open("res/11.dat","rt").read().strip()
  return [[*line] for line in lines.split()]

def formatted(image):
    return "\n".join([''.join(row) for row in image])

def galaxies(universe, expansion):
    expansion -= 1

    empty_cols = [
        i for i, col in enumerate(list(zip(*universe))) 
        if all(x == '.' for x in col)
    ]

    empty_rows = [
        i for i, row in enumerate(universe)
        if all(x == '.' for x in row)
    ]

    retval = []
    for y, row in enumerate(universe):
        for x, col in enumerate(row):
            if col == '#':
                new_x = x + expansion * bisect(empty_cols, x)
                new_y = y + expansion * bisect(empty_rows, y)
                retval.append((new_y, new_x))

    return retval

def distances(gset):
    retval = {}
    pairs = list(combinations(gset, 2))
    for (a,b) in pairs:
        retval[a, b] = abs(a[0] - b[0]) + abs(a[1] - b[1])

    return retval

def part1():
    gset = galaxies(parsedInput(), 2)
    return sum(distances(gset).values())

def part2():
    gset = galaxies(parsedInput(), 1_000_000)
    return sum(distances(gset).values())

if __name__ == '__main__':
  print(part1())
  print(part2())
