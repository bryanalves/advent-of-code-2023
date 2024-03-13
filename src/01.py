import re

def parsedInput():
  lines = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''.rstrip('\n')

  lines = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''.rstrip('\n')

  lines = open("res/01.dat","rt").read().strip()

  splitted = lines.split('\n')
  return splitted

def part1():
  lines = parsedInput()
  numstrings = (re.findall(r'\d', line) for line in lines)
  nums = [int(f"{s[0]}{s[-1]}") for s in numstrings]
  return sum(nums)

def part2():
  lines = parsedInput()
  lines = (line.replace('one', 'o1e') for line in lines)
  lines = (line.replace('two', 't2o') for line in lines)
  lines = (line.replace('three', 't3e') for line in lines)
  lines = (line.replace('four', 'f4r') for line in lines)
  lines = (line.replace('five', 'f5e') for line in lines)
  lines = (line.replace('six', 's6x') for line in lines)
  lines = (line.replace('seven', 's7n') for line in lines)
  lines = (line.replace('eight', 'e8t') for line in lines)
  lines = (line.replace('nine', 'n9e') for line in lines)

  numstrings = (re.findall(r'\d', line) for line in lines)
  nums = [int(f"{s[0]}{s[-1]}") for s in numstrings]
  return sum(nums)

if __name__ == '__main__':
  print(part1())
  print(part2())
