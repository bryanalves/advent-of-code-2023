from itertools import cycle
from math import lcm

def parsedInput():
  lines = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''.rstrip('\n')

  lines = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''.rstrip('\n')

  lines = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''.rstrip('\n')

  lines = open("res/08.dat","rt").read().strip()
  directions, maplines = lines.split('\n\n')

  directions = directions.replace('R', '1').replace('L', '0')
  directions = [int(i) for i in [*directions]]

  maps = dict(build_map(line) for line in maplines.split('\n'))

  return directions, maps

def build_map(line):
    key, vals = line.split(' = ')
    vals = vals[1:9].split(', ')
    return key, vals

def solve(position, directions, maps, endswith):
    steps = 0
    directions = cycle(directions)
    while not position.endswith(endswith):
      steps += 1
      direction = next(directions)
      position = maps[position][direction]

    return steps

def part1():
    directions, maps = parsedInput()
    return solve('AAA', directions, maps, 'ZZZ')

def part2():
    directions, maps = parsedInput()
    positions = [x for x in maps.keys() if x[2] == 'A']
    steps = [solve(p, directions, maps, 'Z') for p in positions]
    return lcm(*steps)

if __name__ == '__main__':
  print(part1())
  print(part2())
