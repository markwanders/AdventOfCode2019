import re

with open("input.txt") as f:
    instructions = [line.rstrip() for line in f]


def deal(cards):
    cards.reverse()
    return cards


def cut(cards, n):
    return cards[n:] + cards[:n]


def increment(cards, n):
    new_cards = cards[:]
    for c in range(len(new_cards)):
        index = (c * n) % len(new_cards)
        new_cards[index] = cards[c]
    return new_cards


deck = list(range(10007))
for instruction in instructions:
    n = re.search(r'-?\d+', instruction)
    if n:
        n = int(n.group())
    if "stack" in instruction:
        deck = deal(deck)
    elif "cut" in instruction:
        deck = cut(deck, n)
    elif "increment" in instruction:
        deck = increment(deck, n)

print(deck.index(2019))
