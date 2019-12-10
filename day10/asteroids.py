with open("input.txt") as f:
    lines = f.read().split()


def collinear(point1, point2, point3):
    return point1[0] * (point2[1] - point3[1]) + \
           point2[0] * (point3[1] - point1[1]) + \
           point3[0] * (point1[1] - point2[1]) == 0


def manhattan(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def between(point1, point2, point3):
    if point1[0] > point2[0]:
        between_x = point2[0] <= point3[0] <= point1[0]
    else:
        between_x = point1[0] <= point3[0] <= point2[0]
    if point1[1] > point2[1]:
        between_y = point2[1] <= point3[1] <= point1[1]
    else:
        between_y = point1[1] <= point3[1] <= point2[1]
    return between_y and between_x


def in_line_of_sight(point1, point2, point3):
    return collinear(point1, point2, point3) and between(point1, point2, point3)


asteroids = set()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            asteroids.add((x, y))

line_of_sight = {a: 0 for a in asteroids}
for asteroid1 in asteroids:
    for asteroid2 in (a for a in asteroids if a != asteroid1):
        if not any([asteroid3 for asteroid3 in (a for a in asteroids if a != asteroid1 and a != asteroid2) if in_line_of_sight(asteroid1, asteroid2, asteroid3)]):
            line_of_sight[asteroid1] += 1
station = max(line_of_sight, key=line_of_sight.get)
print(line_of_sight[station])
