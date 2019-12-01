import math


def fuel_for_mass(m):
    return math.floor(m / 3) - 2


with open("input.txt") as my_file:
    modules = my_file.readlines()
modules = [int(i) for i in modules]

# part 1
fuel = 0
for mass in modules:
    fuel += fuel_for_mass(mass)
print("Total fuel needed is: " + str(fuel))

# part 2
total_fuel = 0
for mass in modules:
    module_fuel = additional_mass = fuel_for_mass(mass)
    while fuel_for_mass(additional_mass) > 0:
        additional_mass = fuel_for_mass(additional_mass)
        module_fuel += additional_mass
    total_fuel += module_fuel
print("Real total fuel needed is: " + str(total_fuel))
