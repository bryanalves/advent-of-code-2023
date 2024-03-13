import math

def parsedInput():
  lines = '''Time:      7  15   30
Distance:  9  40  200
'''.rstrip('\n')

  lines = open("res/06.dat","rt").read().strip()

  splitted = lines.split('\n')
  times = [int(i) for i in splitted[0].split(':')[1].split()]
  distances = [int(i) for i in splitted[1].split(':')[1].split()]

  return zip(times, distances)

def optimize(t, d):
    # brute-force
    # return [i for i in range(t) if (i * (t - i)) > d]

    # x + y = t, x * y < d
    # x**2 - x*t + d < 0
    disc = math.sqrt((t**2) - (4*d))

    min = (t - disc) / 2
    max = (t + disc) / 2

    return range(math.floor(min), math.ceil(max) - 1)

def part1():
    wins = [optimize(time, distance) for time, distance in parsedInput()]
    return math.prod((len(w) for w in wins))

def part2():
    races = list(parsedInput())
    t = ''.join([str(t[0]) for t in races])
    d = ''.join([str(t[1]) for t in races])
    return len(optimize(int(t), int(d)))

if __name__ == '__main__':
  print(part1())
  print(part2())
