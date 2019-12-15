import re

from math import floor

with open("input.txt") as f:
    reactions = [[(re.findall('[A-Z]+', r)[0], int(re.findall(r'\d+', r)[0])) for r in re.findall(r'\d+ [A-Z]+', line)] for line in f.readlines()]
reaction_map = {r[-1]: r[:-1] for r in reactions}


def ore_for_fuel(amount):
    required_chemical_amounts = {'FUEL': amount}

    while [k for (k, v) in required_chemical_amounts.items() if k != "ORE" and v > 0]:
        for chemical in [k for (k, v) in required_chemical_amounts.items() if k != "ORE" and v > 0]:
            output = [k for k in reaction_map.keys() if k[0] == chemical][0]
            quantity = output[1]
            reaction = reaction_map[output]
            multiple = (required_chemical_amounts[chemical] + quantity - 1) // quantity
            for (input_element, input_quantity) in reaction:
                required_chemical_amounts[input_element] = required_chemical_amounts.get(input_element, 0) + multiple * input_quantity
            required_chemical_amounts[chemical] -= multiple * quantity

    return required_chemical_amounts["ORE"]


print(ore_for_fuel(1))

fuel = 1
target = 1e12
while True:
    ore = ore_for_fuel(fuel + 1)
    if ore > target:
        print(fuel)
        break
    else:
        fuel = max(fuel + 1, floor((fuel + 1) * target / ore))
