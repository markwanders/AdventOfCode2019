def fuel_for_mass(m):
    return m // 3 - 2


def iterative_fuel_for_mass(m):
    module_fuel = additional_mass = fuel_for_mass(m)
    while fuel_for_mass(additional_mass) > 0:
        additional_mass = fuel_for_mass(additional_mass)
        module_fuel += additional_mass
    return module_fuel


with open("input.txt") as f:
    modules = [int(i) for i in f.readlines()]

# part 1
fuel = sum([fuel_for_mass(mass) for mass in modules])
print("Total fuel needed is: " + str(fuel))

# part 2
total_fuel = sum([iterative_fuel_for_mass(mass) for mass in modules])
print("Real total fuel needed is: " + str(total_fuel))
