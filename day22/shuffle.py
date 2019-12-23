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


# part one
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

# part two
d = 119315717514047
r = 101741582076661
x = 2020

# since all operations on our deck are linear, there is some a and b for which the position of card x is f(x) = a*x + b
a, b = 1, 0
for instruction in instructions:  # invert all instructions
    n = re.search(r'-?\d+', instruction)
    if n:
        n = int(n.group())
    if "stack" in instruction:
        a *= -1
        b += a
    elif "cut" in instruction:
        b += n * a
    elif "increment" in instruction:
        a *= pow(n, d - 2, d)  # Modular multiplicative inverse via Euler's theorem

a %= d
b %= d
# using geometric series: if f(x) = a*x+b, f^n(x) = x*a^n + b*(1-a^n)/(1-a), all modulo deck size in our case
# n.b.: pow(a, m - 2, m) is the modular multiplicative inverse, i.e. 1/a = a^-1 = a^(m-2) mod(m)
print((pow(a, r, d) * x + b * (1 - pow(a, r, d)) * pow(1 - a, d - 2, d)) % d)
