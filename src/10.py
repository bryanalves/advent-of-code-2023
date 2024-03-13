from collections import Counter

def parsedInput():
  lines = '''..F7.
.FJ|.
SJ.L7
|F--J
LJ...
'''.rstrip('\n')

  lines = '''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
'''.rstrip('\n')


  lines = open("res/10.dat","rt").read().strip()
  return [[*line] for line in lines.split()]

cmap = {
    '|': [(1, 0),  (-1, 0)],
    '-': [(0, 1),  (0, -1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(0, -1), (-1, 0)],
    '7': [(1, 0),  (0, -1)],
    'F': [(1, 0),  (0, 1)],
    'S': [
           (1, 0),  (-1, 0),
           (0, 1),  (0, -1),
         ],
    '.': []
}

def start(animalmap):
    for i, x in enumerate(animalmap):
        if 'S' in x:
            return (i, x.index('S'))

def connections(animalmap, loc):
    max_x = len(animalmap[0])
    max_y = len(animalmap)

    pipe = animalmap[loc[0]][loc[1]]

    return [
        (
            sorted((0, loc[0] + c[0], max_y))[1],
            sorted((0, loc[1] + c[1], max_x))[1],
        )
        for c in cmap[pipe]
    ]

def connects(animalmap, loc, target):
    return target in connections(animalmap, loc)

def build_map(animalmap):
    next = start(animalmap)

    visited = Counter()
    visited[next] = 1

    def run(curpos):
      iteration = visited[curpos] + 1
      cs = [ n for n in connections(animalmap, curpos) ]
      nexts = [ n for n in cs if n not in visited and connects(animalmap, curpos, n) ]

      if not nexts:
        return False

      visited[nexts[0]] = iteration
      return nexts[0]

    while next:
        next = run(next)

    return visited

def shoelace(points):
    area = 0

    X = [point[0] for point in points] + [points[0][0]]
    Y = [point[1] for point in points] + [points[0][1]]

    for i in range(len(points)):
        area += X[i] * Y[i + 1] - Y[i] * X[i + 1]

    return abs(area) // 2

def part1():
    return build_map(parsedInput()).most_common(1)[0][1] // 2

def part2():
    animalmap = parsedInput()
    visited = list(build_map(animalmap).keys())

    area = shoelace([n for n in visited
        if animalmap[n[0]][n[1]] in ["L", "J", "F", "7"]
    ])

    return area + 1 - ((len(visited) - 1) // 2)


if __name__ == '__main__':
  print(part1())
  print(part2())
