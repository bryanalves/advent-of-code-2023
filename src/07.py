from collections import Counter

def parsedInput():
  lines = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''.rstrip('\n')

  lines = open("res/07.dat","rt").read().strip()

  splitted = lines.split('\n')
  return [(line.split()[0], int(line.split()[1])) for line in splitted]

CARD_VALUES = {str(i): i for i in range(2, 10)}
CARD_VALUES['T'] = 10
CARD_VALUES['J'] = 11
CARD_VALUES['Q'] = 12
CARD_VALUES['K'] = 13
CARD_VALUES['A'] = 14

HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIR = 3
THREE_OF_A_KIND = 4
FULL_HOUSE = 5
FOUR_OF_A_KIND = 6
FIVE_OF_A_KIND = 7

def card_values(cards):
    return [CARD_VALUES[c] for c in cards]

def hand_type(cards):
    card_frequencies = [count for _, count in Counter(cards).most_common()]
    return match_on_freq(card_frequencies)

def hand_type_jokers(cards):
    counts = Counter(cards)
    jokers = counts['J']
    if jokers in range(1, 5):
        del counts['J']
        counts[counts.most_common(1)[0][0]] += jokers

    card_frequencies = [count for _, count in counts.most_common()]
    return match_on_freq(card_frequencies)

def match_on_freq(freqs):
    match freqs:
        case [5, *_]:
            return FIVE_OF_A_KIND
        case [4, *_]:
            return FOUR_OF_A_KIND
        case [3, 2, *_]:
            return FULL_HOUSE
        case [3, *_]:
            return THREE_OF_A_KIND
        case [2, 2, *_]:
            return TWO_PAIR
        case [2, *_]:
            return ONE_PAIR
        case _ :
            return HIGH_CARD


def part1():
  def order_hand(hand):
    return hand_type(hand[0]), card_values(hand[0])

  hands = parsedInput()
  hands.sort(key=order_hand)
  return (sum(i * hand[1] for i, hand in enumerate(hands, 1)))

def part2():
  def order_hand(hand):
    return hand_type_jokers(hand[0]), card_values(hand[0])

  CARD_VALUES['J'] = 0
  hands = parsedInput()
  hands.sort(key=order_hand)
  return (sum(i * hand[1] for i, hand in enumerate(hands, 1)))

if __name__ == '__main__':
  print(part1())
  print(part2())
