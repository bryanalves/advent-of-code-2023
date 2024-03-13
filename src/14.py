def parsedInput():
  lines = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''.rstrip('\n')

  lines = open("res/14.dat","rt").read().strip()
  return tuple(lines.split('\n'))

def shift_north(puzzle):
    lines = zip(*puzzle)
    lines = shift(lines)
    return zip(*lines)

def shift_west(puzzle):
    return shift(puzzle)

def shift_south(puzzle):
    puzzle = ( p[::-1] for p in zip(*puzzle) )
    puzzle = shift(puzzle)
    return zip(*[p[::-1] for p in puzzle])

def shift_east(puzzle):
    puzzle = ( p[::-1] for p in puzzle )
    puzzle = shift(puzzle)
    return ( p[::-1] for p in puzzle )

def shift(lines):
    return ['#'.join(
        [f"{'O' * s.count('O')}{'.' * s.count('.')}" for s in ''.join(line).split('#')]
    ) for line in lines]

def shift_all(puzzle):
    puzzle = shift_north(puzzle)
    puzzle = shift_west(puzzle)
    puzzle = shift_south(puzzle)
    puzzle = shift_east(puzzle)
    return tuple(puzzle)

def score(puzzle):
    return sum([scorecol(col) for col in zip(*puzzle)])

def scorecol(col):
    return sum([len(col) - i for i, el in enumerate(col) if el == 'O'])

def part1():
    return score(shift_north(parsedInput()))

def part2():
    puzzle = parsedInput()
    seen = {}
    times = 1_000_000_000

    i = 0
    while puzzle not in seen:
        seen[puzzle] = i
        puzzle = shift_all(puzzle)
        i += 1

    period = i - seen[puzzle]
    rest = (times - i) % period

    for _ in range(rest):
        puzzle = shift_all(puzzle)

    return score(puzzle)

if __name__ == '__main__':
  print(part1())
  print(part2())
