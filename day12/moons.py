import re
import itertools
from fractions import gcd

with open("input.txt") as f:
    moons = [map(int, re.findall(r'-?\d+', line)) for line in f.readlines()]

positions = {i: moons[i] for i in range(len(moons))}
velocities = {i: [0] * len(positions[0]) for i in range(len(moons))}
repeats = [0] * len(positions[0])

step = 1
proceed = True
while any(i == 0 for i in repeats):
    for pair in itertools.combinations(positions.keys(), 2):
        position1, position2 = positions[pair[0]], positions[pair[1]]
        velocities1, velocities2 = velocities[pair[0]], velocities[pair[1]]
        for d, position in enumerate(position1):
            if position > position2[d]:
                velocities1[d] -= 1
                velocities2[d] += 1
            elif position < position2[d]:
                velocities1[d] += 1
                velocities2[d] -= 1
    positions = {moon: [sum(pv) for pv in zip(positions[moon], velocities[moon])] for moon in positions.keys()}
    for d, repeat in enumerate(repeats):
        if repeat == 0 and all((positions[m][d], velocities[m][d]) == (moons[m][d], 0) for m in positions.keys()):
            repeats[d] = step
    # part one
    if step == 1000:
        print(sum([sum(map(abs, positions[moon])) * sum(map(abs, velocities[moon])) for moon in positions.keys()]))
    step += 1

# part two: calculate lowest common multiple of repeating coordinate states
lcm = repeats[0]
for repeat in repeats[1:]:
    lcm = lcm * repeat / gcd(lcm, repeat)
print(lcm)
