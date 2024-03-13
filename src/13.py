from itertools import pairwise, chain

def parsedInput():
  lines = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
'''.rstrip('\n')

  lines = open("res/13.dat","rt").read().strip()
  puzzles = [puzzle.split('\n') for puzzle in lines.split('\n\n')]

  return puzzles

def smudged(s1, s2):
  return 1 == sum(1 for c1, c2 in zip(s1, s2) if c1 != c2)

def is_mirror(a, b, lines, fixes_remaining):
    while a >= 0 and b < len(lines):
        al, bl = lines[a][1], lines[b][1]
        if bl != al:
            if smudged(bl, al) and fixes_remaining:
                fixes_remaining -= 1
            else:
                return False
        a -= 1
        b += 1

    return fixes_remaining == 0

def solve(puzzle, fixes_remaining):
    cols = list(enumerate(list(zip(*puzzle))))
    rows = list(enumerate(puzzle))

    return next(chain(
     (a[0] + 1 for a, b in pairwise(cols) if is_mirror(a[0], b[0], cols, fixes_remaining)),
     ((a[0] + 1) * 100 for a, b in pairwise(rows) if is_mirror(a[0], b[0], rows, fixes_remaining))
    ))

def part1():
    return sum(solve(p, 0) for p in parsedInput())

def part2():
    return sum(solve(p, 1) for p in parsedInput())

if __name__ == '__main__':
  print(part1())
  print(part2())

