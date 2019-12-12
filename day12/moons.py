import re
import itertools

with open("input.txt") as f:
    moons = [map(int, re.findall(r'-?\d+', line)) for line in f.readlines()]

positions = {i: moons[i] for i in range(len(moons))}
velocities = {i: [0, 0, 0] for i in range(len(moons))}

for step in range(1000):
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

print(sum([sum(map(abs, positions[moon])) * sum(map(abs, velocities[moon])) for moon in positions.keys()]))
