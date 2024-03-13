import itertools

def parsedInput():
  lines = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''.rstrip('\n')

  lines = open("res/09.dat","rt").read().strip()
  return [[int(i) for i in line.split(' ')] for line in lines.split('\n')]

def prednext(i):
    retval = 0 
    while any(x != 0 for x in i):
        retval += i[-1]
        i = [b - a for a,b in itertools.pairwise(i)]

    return retval

def part1():
    return sum(prednext(i) for i in parsedInput())

def part2():
    return sum(prednext(i[::-1]) for i in parsedInput())

if __name__ == '__main__':
  print(part1())
  print(part2())
