import re
from itertools import product, repeat
import functools

def parsedInput():
  lines = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''.rstrip('\n')

  lines = open("res/12.dat","rt").read().strip()

  splitted = lines.split('\n')
  splitted = [line.split(' ') for line in splitted]
  return [(
    line[0],
    tuple(map(int, line[1].split(',')))
  ) for line in splitted]

@functools.cache
def solve3(pattern, segments):
    if len(segments) == 0:
        if "#" in pattern:
            return 0
        return 1

    curr = segments[0]
    paths = 0

    for i in range(len(pattern) - sum(segments[1:])):
        for j in range(i, i + curr):
            if j == i and j > 0 and pattern[j - 1] == "#":
                return paths
            if j >= len(pattern):
                return paths
            # invalid
            if pattern[j] == ".":
                break
            # valid path found
            if j == i + curr - 1:
                # conflicting ending
                if j + 1 < len(pattern) and pattern[j + 1] == "#":
                    break
                # happy path
                paths += solve3(pattern[j + 2 :], segments[1:])

    return paths

@functools.cache
def solve2(pattern: str, counts: tuple[int]) -> int:
    # base case
    if not pattern:
        return len(counts) == 0

    if not counts:
        return "#" not in pattern

    result = 0

    if pattern[0] in ".?":
        result += solve2(pattern[1:], counts)

    if (
        pattern[0] in "#?"
        and counts[0] <= len(pattern)
        and "." not in pattern[: counts[0]]
        and (counts[0] == len(pattern) or pattern[counts[0]] != "#")
    ):
        result += solve2(pattern[counts[0] + 1 :], counts[1:])

    return result

def solve(row, pattern):
    def advance(i, j):
        if j >= len(pattern):
          return 0
        if len(row) - i < pattern[j]:
          return 0
        if '.' in row[i:i+pattern[j]]:
          return 0
        if len(row) - i == pattern[j]:
          return dp(len(row), j+1)

        return dp(i+pattern[j]+1, j+1) if row[i+pattern[j]] in '.?' else 0

    @functools.cache
    def dp(i, j):
        if i >= len(row):
          return j >= len(pattern)
        if row[i] == '.':
          return dp(i+1, j)
        if row[i] == '#':
          return advance(i, j)
        return dp(i+1, j) + advance(i, j)
    return dp(0, 0)

def part1():
    lines = parsedInput()
    return sum(solve(row, pattern) for row,pattern in lines)

def part2():
    lines = parsedInput()
    lines = [(
      '?'.join([row] * 5),
      pattern * 5
    ) for row, pattern in lines]

    return sum(solve(row, pattern) for row,pattern in lines)

if __name__ == '__main__':
  print(part1())
  print(part2())
