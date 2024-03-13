import re
from collections import defaultdict
import math

def parsedInput():
  lines = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''.rstrip('\n')

#   lines = '''..........
# 467..114..
# *.........
# '''.rstrip('\n')

  lines = open("res/03.dat","rt").read().strip()

  splitted = lines.split('\n')
  return splitted

def part_numbers(input):
  retval = []
  matcher = re.compile(r"\d+")
  for n, line in enumerate(input):
    for m in matcher.finditer(line):
      part = m.group()
      retval.append((int(part), n, m.start(), m.start() + len(part) - 1))

  return retval

def symbols(input):
  ret = defaultdict(list)
  matcher = re.compile(r"[^\d\.]")
  for n, line in enumerate(input):
    for m in matcher.finditer(line):
      ret[n].append((m.start(), m.group()))

  return ret

def matched_parts(nums, parts):
    matching_nums = []
    gears = defaultdict(list)
    for x in nums:
      num, row, start, end = x
      r = range(start - 1, end + 2)

      parts_above = parts.get(row - 1) or []
      parts_cur = parts.get(row) or []
      parts_below = parts.get(row + 1) or []

      match_above = [(row-1, p[0], p[1]) for p in parts_above if p[0] in r]
      match_cur = [(row, p[0], p[1]) for p in parts_cur if p[0] in r]
      match_below = [(row+1, p[0], p[1]) for p in parts_below if p[0] in r]
      matches = match_above + match_cur + match_below
      matching_gears = [g[0:2] for g in matches if g[2] == '*']
      for g in matching_gears:
        gears[g].append(num)
      if any(matches):
        matching_nums.append(num)

    return (matching_nums, gears)

def part1():
    parsed = parsedInput()
    nums = part_numbers(parsed)
    parts = symbols(parsed)
    # print(nums.keys())
    # print(matched_parts(nums, parts))
    return sum(matched_parts(nums, parts)[0])

def part2():
    parsed = parsedInput()
    nums = part_numbers(parsed)
    parts = symbols(parsed)

    gears = matched_parts(nums, parts)[1]
    return sum(math.prod(vals) for vals in gears.values() if len(vals) == 2)

if __name__ == '__main__':
  print(part1())
  print(part2())
