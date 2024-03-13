import re
from functools import reduce

def parsedInput():
  sequences = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''
  sequences = open("res/15.dat","rt").read().strip()
  return sequences.split(',')

def hash(s):
    return reduce(lambda acc, c: ((acc + ord(c)) * 17) % 256,
                  s, 0)

def runtape(sequences):
    tape = [{} for _ in range(256)]

    for s in sequences:
        label, op = re.split(r'[=-]', s)
        box = hash(label)
        if not len(op):
            tape[box].pop(label, None)
        else:
            tape[box][label] = int(op)

    return tape

def fpower(tape):
    return [
        lens * idx * boxnum
        for boxnum, items in enumerate(tape, 1)
        for idx, lens in enumerate(items.values(), 1)
    ]

def part1():
    return sum([hash(seq) for seq in parsedInput()])

def part2():
    return sum(fpower(runtape(parsedInput())))

if __name__ == '__main__':
  print(part1())
  print(part2())
