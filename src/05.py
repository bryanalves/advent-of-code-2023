import multiprocessing
from functools import partial
from pprint import pprint
import re

def parsedInput():
  lines = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''.rstrip('\n')

  lines = open("res/05.dat","rt").read().strip()

  def build_range(inp):
    parsed = [[int(i) for i in line.split()] for line in inp.split('\n')[1:]]
    ranges = []
    for mp in parsed:
        ranges.append((
                range(mp[1], mp[1] + mp[2]),
                range(mp[0], mp[0] + mp[2])
            ))
    return ranges

  groups = lines.split('\n\n')
  seeds = [int(i) for i in groups[0].split(': ')[1].split()]
  seed_to_soil = build_range(groups[1])
  soil_to_fertilizer = build_range(groups[2])
  fertilizer_to_water = build_range(groups[3])
  water_to_light = build_range(groups[4])
  light_to_temperature = build_range(groups[5])
  temperature_to_humidity = build_range(groups[6])
  humidity_to_location = build_range(groups[7])

  return (
    seeds,
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location
    )

def find_dest(inp, target):
  for rng in target:
    if inp in rng[0]:
      diff = inp - rng[0][0]
      return rng[1][0] + diff
  return inp

def map_thru(groups, seed):
  print(seed)
  retval = seed
  for i in groups:
    retval = find_dest(retval, i)
  return retval

def part1():
  parsed = parsedInput()
  # return(map_thru(parsed[0][0], parsed[1:]))
  return(min([map_thru(parsed[1:], seed) for seed in parsed[0]]))

def _part2():
  parsed = parsedInput()
  seeds = parsed[0]
  seeds = zip(seeds[::2], seeds[1::2])
  seed_ranges = [range(s[0], s[0] + s[1]) for s in seeds]
  pool = multiprocessing.Pool()
  new_map_thru = partial(map_thru, parsed[1:])
  range_mins = [min(pool.map(new_map_thru, seed_range)) for seed_range in seed_ranges]
  # range_mins = [min([map_thru(seed, parsed[1:]) for seed in seed_range] for seed_range in seed_ranges)]
  return min(range_mins)

def map_range(group, seed_range):
    ranges, i = [], 0

    while True:
        g_range = group[i]

        if seed_range[0] < g_range[0][0]:
            if seed_range[1] < g_range[0][0]:
                ranges.append(seed_range)
                return ranges
            ranges.append((seed_range[0], g_range[0][0] - 1))
            seed_range = g_range[0][0], seed_range[1]

        elif g_range[0][0] <= seed_range[0] < g_range[0][-1]:
            offset = g_range[1][0] - g_range[0][0]
            if seed_range[1] < g_range[0][-1]:
                ranges.append(tuple(r + offset for r in seed_range))
                return ranges
            ranges.append((seed_range[0] + offset, g_range[1][-1]))
            seed_range = g_range[0][-1] + 1, seed_range[1]

        elif g_range[0][-1] <= seed_range[0]:
            i += 1
            if i == len(group):
                break

    ranges.append(seed_range)
    return ranges

def part2():
  parsed = parsedInput()
  seeds = parsed[0]
  # seeds = zip(seeds[::2], seeds[1::2])
  # seed_ranges = [range(s[0], s[0] + s[1]) for s in seeds]
  seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

  for group in parsed[1:]:
    group = sorted(group, key=lambda x: x[0][0])
    seed_ranges = sum((map_range(group, rng) for rng in seed_ranges), [])

  return next(map(min, zip(*seed_ranges)))

if __name__ == '__main__':
  # print(part1())
  print(part2())

  # with open("res/05.dat", "r") as f:
  #       res = f.read().strip().split("\n\n")
  #       seeds = list(map(int, re.findall("\d+", res[0])))
  #       ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
  #       for cs in res[1:]:
  #           c = list(map(int, re.findall("\d+", cs)))
  #           # sort for part 2
  #           cv = sorted([c[k : k + 3] for k in range(0, len(c), 3)], key=lambda x: x[1])
  #           print(cv)
  #           break
