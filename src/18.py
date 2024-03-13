def parsedInput():
  lines = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
'''.rstrip('\n')

  lines = open("res/18.dat","rt").read().strip()

  lines = [line.split(' ') for line in lines.split('\n')]
  lines = [(line[0], int(line[1]), line[2][2:-1]) for line in lines]
  return lines

def area(directions):
    pos = (0, 0)
    perimeter = 0
    corners = []
    dirmap = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    for dir, dist in directions:
        dy, dx = dirmap[dir]
        pos = (pos[0] + dy * dist, pos[1] + dx * dist)
        perimeter += dist
        corners.append(pos)

    return shoelace(corners) + perimeter // 2 + 1

def shoelace(points):
    result = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        result += x1 * y2 - x2 * y1

    return abs(result) // 2

def decode(h):
    dirmap = {
        0: 'R',
        1: 'D',
        2: 'L',
        3: 'U'
    }

    return dirmap[int(h[5], 16)], int(h[0:5], 16)

def part1():
    directions = [(d[0], d[1]) for d in parsedInput()]
    return area(directions)

def part2():
    directions = [decode(d[2]) for d in parsedInput()]
    return area(directions)

if __name__ == '__main__':
    print(part1())
    print(part2())
