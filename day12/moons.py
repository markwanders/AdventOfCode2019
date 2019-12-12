import re
import itertools
from fractions import gcd

with open("input.txt") as f:
    moons = [map(int, re.findall(r'-?\d+', line)) for line in f.readlines()]

positions = {i: moons[i] for i in range(len(moons))}
velocities = {i: [0, 0, 0] for i in range(len(moons))}
repeats = [0, 0, 0]

step = 1
proceed = True
while any(i == 0 for i in repeats):
    for pair in itertools.combinations(positions.keys(), 2):
        position1, position2 = positions[pair[0]], positions[pair[1]]
        for c in range(3):
            if position1[c] > position2[c]:
                velocities[pair[0]][c] -= 1
                velocities[pair[1]][c] += 1
            elif position1[c] < position2[c]:
                velocities[pair[0]][c] += 1
                velocities[pair[1]][c] -= 1
    for moon in positions.keys():
        positions[moon] = [sum(x) for x in zip(positions[moon], velocities[moon])]
    for c in range(3):
        if repeats[c] == 0 and all((positions[m][c], velocities[m][c]) == (moons[m][c], 0) for m in positions.keys()):
            repeats[c] = step
    # part one
    if step == 1000:
        print(sum([sum(map(abs, positions[moon])) * sum(map(abs, velocities[moon])) for moon in positions.keys()]))
    step += 1

# part two: calculate lowest common multiple of repeating coordinate states
lcm = repeats[0]
for repeat in repeats[1:]:
    lcm = lcm * repeat / gcd(lcm, repeat)
print(lcm)
