from itertools import chain
from functools import partial
import multiprocessing

def parsedInput():
  lines = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
'''.rstrip('\n')

  lines = open("res/16.dat","rt").read().strip()
  return lines.split('\n')

def energize(grid, startbeam):
    beams = [startbeam]
    visited = set(beams)

    while len(beams):
        b = beams.pop()
        newbeams = movebeam(grid, b)
        for b in newbeams:
          if b not in visited:
            visited.add(b)
            beams.append(b)

    return len(set([(v[0], v[1]) for v in visited]))

def movebeam(grid, beam):
    y, x, diry, dirx = beam
    newbeam = None
    tile = grid[y][x]

    if tile == '/':
        diry, dirx = -dirx, -diry

    if tile == "\\":
        diry, dirx = dirx, diry

    if tile == '-' and dirx == 0:
        diry, dirx = 0, 1
        newbeam = (y, x - 1, 0, -1)

    if tile == '|' and diry == 0:
        diry, dirx = 1, 0
        newbeam = (y - 1, x, -1, 0)

    y += diry
    x += dirx

    retval = []
    if y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0]):
        retval.append((y, x, diry, dirx))
    if newbeam and newbeam[0] >= 0 and newbeam[0] < len(grid) and newbeam[1] >= 0 and newbeam[1] < len(grid[0]):
        retval.append(newbeam)

    return retval

def part1():
    return energize(parsedInput(), (0, 0, 0, 1))

def part2():
    grid = parsedInput()

    tr = ( (0, x,  1,  0) for x in range(len(grid[0])) )
    br = ( (0, x, -1,  0) for x in range(len(grid[0])) )
    lc = ( (y, 0,  0,  1) for y in range(len(grid)) )
    rc = ( (y, 0,  0, -1) for y in range(len(grid)) )

    return max(multiprocessing.Pool().map(
        partial(energize, grid),
        chain(tr, br, lc, rc)
    ))

if __name__ == '__main__':
  print(part1())
  print(part2())
