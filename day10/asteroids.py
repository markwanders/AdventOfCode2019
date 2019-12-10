with open("input.txt") as f:
    lines = f.read().split()


def collinear(point1, point2, point3):
    return point1[0] * (point2[1] - point3[1]) + \
           point2[0] * (point3[1] - point1[1]) + \
           point3[0] * (point1[1] - point2[1]) == 0


def manhattan(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def in_line_of_sight(point1, point2, point3):
    return collinear(point1, point2, point3) and manhattan(point1, point3) < manhattan(point1, point2)


asteroids = []
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            asteroids.append((x, y))

line_of_sight = {a: 0 for a in asteroids}
for asteroid1 in asteroids:
    for asteroid2 in (a for a in asteroids if a != asteroid1):
        if not any([asteroid3 for asteroid3 in (a for a in asteroids if a != asteroid1) if in_line_of_sight(asteroid1, asteroid2, asteroid3)]):
            line_of_sight[asteroid1] += 1
print(max(line_of_sight, key=line_of_sight.get), line_of_sight[max(line_of_sight, key=line_of_sight.get)])
