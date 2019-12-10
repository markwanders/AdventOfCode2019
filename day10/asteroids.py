with open("input.txt") as f:
    lines = f.read().split()


def collinear(point1, point2, point3):
    return point1[0] * (point2[1] - point3[1]) + \
           point2[0] * (point3[1] - point1[1]) + \
           point3[0] * (point1[1] - point2[1]) == 0


def between(point1, point2, point3):
    return (point2[0] <= point3[0] <= point1[0] or point1[0] <= point3[0] <= point2[0]) and (point2[1] <= point3[1] <= point1[1] or point1[1] <= point3[1] <= point2[1])


def in_line_of_sight(point1, point2, point3):
    return collinear(point1, point2, point3) and between(point1, point2, point3)


asteroids = set()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            asteroids.add((x, y))

line_of_sight = {a: [] for a in asteroids}
for asteroid1 in asteroids:
    for asteroid2 in (a for a in asteroids if a != asteroid1):
        if not any([asteroid3 for asteroid3 in (a for a in asteroids if a != asteroid1 and a != asteroid2) if in_line_of_sight(asteroid1, asteroid2, asteroid3)]):
            line_of_sight[asteroid1].append(asteroid2)
station = max(line_of_sight, key=lambda v: len(line_of_sight[v]))
print(len(line_of_sight[station]))
