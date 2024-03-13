from math import lcm
from itertools import count

def parsedInput():
    lines = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
'''.rstrip('\n')

    lines = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
'''.rstrip('\n')

    lines = open("res/20.dat","rt").read().strip()
    mappings = lines.split('\n')
    mappings = [m.split(' -> ') for m in mappings]

    statemap = {}
    connections = {}

    for module, clist in mappings:
        module_name = ''

        if module == 'broadcaster':
            module_name = 'broadcaster'
            statemap[module_name] = ('B', None)
        else:
            mtype, module_name = module[0], module[1:]
            state = None
            match mtype:
                case '%':
                    state = False
                case '&':
                    state = {}
            statemap[module_name] = [mtype, state]

        cs = clist.split(', ')
        connections[module_name] = cs

    for source, targets in connections.items():
        conjunctors = [t for t in targets if statemap.get(t, ["", ""])[0] == '&']
        for c in conjunctors:
            statemap[c][1][source] = 0


    return statemap, connections

def change(connections, state, source, pulse, target):
    queue = []

    module = state.get(target, None)
    if not module:
        return queue

    if module[0] == '%' and not pulse:
        module[1] = not module[1]
        newpulse = module[1]

        for m in connections[target]:
            queue.append((target, newpulse, m))

    if module[0] == '&':
        module[1][source] = pulse
        newpulse = not all(module[1].values())

        for m in connections[target]:
            queue.append((target, newpulse, m))

    if module[0] == 'B':
        for m in connections[target]:
            queue.append((target, pulse, m))

    return queue

def button(connections, state):
    queue = [('button', False, 'broadcaster')]
    pulses = []

    while queue:
        pulse = queue.pop(0)
        pulses.append(pulse)
        extra = change(connections, state, *pulse)
        queue.extend(extra)

    return pulses

def part1():
    state, connections = parsedInput()

    lowcount = 0
    highcount = 0

    for _ in range(1000):
        pulses = button(connections, state)
        lowcount += sum(1 for p in pulses if not p[1])
        highcount += sum(1 for p in pulses if p[1])

    return highcount * lowcount

def part2():
    state, connections = parsedInput()

    nand = [s for s, dests in connections.items() if 'rx' in dests][0]
    watch = (s for s, dests in connections.items() if nand in dests)
    watch = {x: 0 for x in watch}

    for i in count(1):
        pulses = button(connections, state)
        for p in pulses:
            if p[1] and p[0] in watch.keys() and not watch[p[0]]:
                watch[p[0]] = i
        if all(watch.values()):
            return lcm(*watch.values())

if __name__ == '__main__':
    print(part1())
    print(part2())
