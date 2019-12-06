with open("input.txt") as f:
    orbits_input = f.read().splitlines()

orbits = {}


def count_orbits(obj):
    counter = 0
    while obj in orbits.keys():
        obj = orbits[obj]
        counter += 1
    return counter


for orbit in orbits_input:
    a, b = orbit.split(")")
    orbits[b] = a

# part one
number_of_orbits = sum([count_orbits(planet) for planet in orbits.keys()])
print(number_of_orbits)


# part two
def traverse(path):
    while path[-1] in orbits.keys():
        path.append(orbits[path[-1]])
    return path


print(len(set(traverse([orbits["SAN"]])) ^ set(traverse([orbits["YOU"]]))))
