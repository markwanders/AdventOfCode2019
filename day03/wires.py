with open("input.txt") as f:
    wire1 = f.readline().split(",")
    wire2 = f.readline().split(",")


def calculate_lines(wire):
    locations = [(0, 0)]
    for direction in wire:
        steps = int(direction[1:])
        location = locations[-1]
        if direction.startswith("L"):
            locations.extend((x, location[1]) for x in range(location[0] - 1, location[0] - steps - 1, -1))
        elif direction.startswith("R"):
            locations.extend((x, location[1]) for x in range(location[0] + 1, location[0] + steps + 1))
        elif direction.startswith("U"):
            locations.extend((location[0], y) for y in range(location[1] + 1, location[1] + steps + 1))
        elif direction.startswith("D"):
            locations.extend((location[0], y) for y in range(location[1] - 1, location[1] - steps - 1, -1))
    return locations


locations1 = calculate_lines(wire1)
locations2 = calculate_lines(wire2)

intersects = set(locations1[1:]) & set(locations2[1:])

manhattan_distances = [abs(intersection[0]) + abs(intersection[1]) for intersection in intersects]

# part one
print(min(manhattan_distances))

# part two
step_distance = [locations1.index(intersection) + locations2.index(intersection) for intersection in intersects]
print(min(step_distance))
