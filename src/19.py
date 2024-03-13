from pprint import pprint
from copy import deepcopy
import functools

def parsedInput():
  lines = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
'''.rstrip('\n')

  lines = open("res/19.dat","rt").read().strip()

  workflows, parts = lines.split("\n\n")
  wf_map = {}
  for workflow in workflows.split("\n"):
        name, rest = workflow.split('{')
        rules = rest[:-1].split(',')
        rules[-1] = f"True:{rules[-1]}"
        rules = [tuple(r.split(':')) for r in rules]
        wf_map[name] = rules

  parts_parsed = []
  for p in parts.split('\n'):
        params = p[1:-1].split(',')
        params = [p.split('=') for p in params]
        params = [(p[0], int(p[1])) for p in params]
        parts_parsed.append(dict(params))

  return wf_map, parts_parsed

def evaluate(part, rules):
    x, m, a, s = part['x'], part['m'], part['a'], part['s']
    for check, dest in rules:
        if eval(check):
            return dest

def runpart(part, workflows):
    flow = 'in'
    while flow not in ('A', 'R'):
        flow = evaluate(part, workflows[flow])
    return flow == 'A'

def process(workflows, start, default_ranges, candidates):
    rules = workflows[start]

    default_dest = rules[-1][1]
    rules = rules[0:-1]

    for check, dest in rules:
        new_ranges = apply_rule(deepcopy(default_ranges), check)
        default_ranges = exclude_rule(default_ranges, check)

        if dest == 'A':
            candidates.append(new_ranges)
        elif dest != 'R':
            candidates = process(workflows, dest, new_ranges, candidates)

    if default_dest == 'A':
        candidates.append(default_ranges)
    elif default_dest != 'R':
        candidates = process(workflows, default_dest, default_ranges, candidates)

    return candidates

def apply_rule(ranges, rule):
    var = rule[0]
    compare = rule[1]
    val = int(rule[2:])

    if compare == '<':
        ranges[var][1] = min(ranges[var][1], val - 1)
    else:
        ranges[var][0] = max(ranges[var][0], val + 1)

    return ranges

def exclude_rule(ranges, rule):
    var = rule[0]
    compare = rule[1]
    val = int(rule[2:])

    if compare == '>':
        ranges[var][1] = min(ranges[var][1], val)
    else:
        ranges[var][0] = max(ranges[var][0], val)

    return ranges

def combos(rangeset):
    return functools.reduce(lambda a, x: a * (x[1] - x[0] + 1), rangeset.values(), 1)

def part1():
    workflows, parts = parsedInput()
    accepted = []
    for part in parts:
        if runpart(part, workflows):
            accepted.append(part)

    return sum(sum(p.values()) for p in accepted)

def part2():
    workflows, _ = parsedInput()

    ranges = {
        'x': [1, 4000],
        'm': [1, 4000],
        'a': [1, 4000],
        's': [1, 4000]
    }

    accepts = process(workflows, 'in', ranges, [])
    return sum([combos(r) for r in accepts])

if __name__ == '__main__':
    print(part1())
    print(part2())
