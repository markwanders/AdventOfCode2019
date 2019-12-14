import re

with open("input.txt") as f:
    reactions = [[(re.findall('[A-Z]+', r)[0], int(re.findall(r'\d+', r)[0])) for r in re.findall(r'\d+ [A-Z]+', line)] for line in f.readlines()]
reaction_map = {r[-1]: r[:-1] for r in reactions}
inventory = {r[0]: 0 for r in reaction_map.keys()}
inventory["ORE"] = ore = 0


def react(output, inputs):
    global ore
    for c in inputs:
        while inventory[c[0]] < c[1]:
            if c[0] == "ORE":
                ore += c[1] - inventory[c[0]]
                inventory["ORE"] = c[1]
            else:
                new_output = [k for k in reaction_map.keys() if c[0] in k][0]
                new_input = reaction_map[new_output]
                react(new_output, new_input)
        inventory[c[0]] -= c[1]
    inventory[output[0]] += output[1]


react(('FUEL', 1), reaction_map[('FUEL', 1)])
print(ore)
