from collections import defaultdict
import math

def parsedInput():
  lines = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''.rstrip('\n')

  lines = open("res/02.dat","rt").read().strip()

  splitted = lines.split('\n')
  return splitted

def build_max(sampleset):
    ret = defaultdict(list)
    for samples in sampleset:
        for color, count in samples.items():
          ret[color].append(count)
    return [max(counts) for counts in ret.values()]

def match_samples(samples, target):
    for color, count in samples.items():
        if count > target[color]:
            return False
    return True

def build_games(input):
  def build(samples):
      samples = [s.split()[::-1] for s in samples]
      samples = [[s[0], int(s[1])] for s in samples]
      return dict(samples)

  games = {}
  for line in input:
    game, sampleset = line.split(': ')
    game = int(game.split(' ')[1])
    sampleset = [
        samples.split(', ')
        for samples in sampleset.split('; ')
    ]
    sampleset = [build(samples) for samples in sampleset]
    games[game] = sampleset

  return games

def part1():
  games = build_games(parsedInput())
  target = {'red': 12, 'green': 13, 'blue': 14}

  filtered = {}
  for game, sampleset in games.items():
      if all((match_samples(samples, target) for samples in sampleset)):
            filtered[game] = sampleset

  return sum(filtered.keys())

def part2():
  games = build_games(parsedInput())
  return sum([math.prod(build_max(sampleset)) for sampleset in games.values()])

if __name__ == '__main__':
  print(part1())
  print(part2())
