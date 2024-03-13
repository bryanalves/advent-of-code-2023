from collections import deque, defaultdict

def parsedInput():
    lines = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
'''.rstrip('\n')

    lines = open("res/22.dat","rt").read().strip()
    lines = [list(map(int, line.replace('~', ',').split(','))) for line in lines.split('\n')]
    lines.sort(key = lambda x: x[2])
    return lines

def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) \
       and max(a[1], b[1]) <= min(a[4], b[4])

def move(bricks):
    for index, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:index]:
            if overlaps(brick, check):
                max_z = max(max_z, check[5] + 1)

        brick[5] -= brick[2] - max_z
        brick[2] = max_z

    bricks.sort(key=lambda brick: brick[2])

def build_adjacency(bricks):
    move(bricks)

    k_supports_v = defaultdict(set)
    v_supports_k = defaultdict(set)

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supports_v[i].add(j)
                v_supports_k[j].add(i)

    return k_supports_v, v_supports_k

def simulate(i, k_supports_v, v_supports_k):
    q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
    falling = set(q)
    falling.add(i)

    while q:
        j = q.popleft()
        for k in k_supports_v[j] - falling:
            if v_supports_k[k] <= falling:
                q.append(k)
                falling.add(k)

    return len(falling) - 1

def part1():
    bricks = parsedInput()
    k_supports_v, v_supports_k = build_adjacency(parsedInput())

    return sum([1 for i in range(len(bricks))
        if all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i])])

def part2():
    bricks = parsedInput()
    k_supports_v, v_supports_k = build_adjacency(bricks)

    return sum([simulate(i, k_supports_v, v_supports_k) for i in range(len(bricks))])

if __name__ == '__main__':
    print(part1())
    print(part2())
