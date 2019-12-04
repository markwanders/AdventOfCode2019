with open("input.txt") as f:
    wire1 = f.readline().split(",")
    wire2 = f.readline().split(",")


def calculate_lines(wire):
    locations = [(0, 0)]
    for direction in wire:
        steps = int(direction[1:])
        current_location = locations[-1]
        if direction.startswith("L"):
            for x in range(current_location[0] - 1, current_location[0] - steps - 1, -1):
                locations.append((x, current_location[1]))
        elif direction.startswith("R"):
            for x in range(current_location[0] + 1, current_location[0] + steps + 1):
                locations.append((x, current_location[1]))
        elif direction.startswith("U"):
            for y in range(current_location[1] + 1, current_location[1] + steps + 1):
                locations.append((current_location[0], y))
        elif direction.startswith("D"):
            for y in range(current_location[1] - 1, current_location[1] - steps - 1, -1):
                locations.append((current_location[0], y))
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
