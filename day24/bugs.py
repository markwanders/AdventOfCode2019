# part one
grid = {}

with open("input.txt") as f:
    y = 0
    for _y in [line.rstrip() for line in f]:
        x = 0
        for _x in _y:
            grid[(y, x)] = _x
            x += 1
        y += 1


def adjacent_bugs(point, grid):
    adjacent_points = [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]
    return len([p for p in adjacent_points if grid.get(p, '.') == '#'])


def biodiversity(grid):
    n = 0
    bio = 0
    for point in sorted(grid.keys()):
        if grid[point] == '#':
            bio += 2**n
        n += 1
    return bio


biodiversities = set()
while True:
    biodiversity_for_grid = biodiversity(grid)
    if biodiversity_for_grid in biodiversities:
        print(biodiversity_for_grid)
        break
    biodiversities.add(biodiversity_for_grid)
    adjacent = {k: adjacent_bugs(k, grid) for k in grid.keys()}
    for point in grid.keys():
        if grid[point] == '#' and adjacent[point] != 1:
            grid[point] = '.'
        elif grid[point] == '.' and 0 < adjacent[point] <= 2:
            grid[point] = '#'

# part two
grids = {}

with open("input.txt") as f:
    y = 0
    for _y in [line.rstrip() for line in f]:
        x = 0
        for _x in _y:
            grids[(y, x, 0)] = _x
            x += 1
        y += 1


def recursive_adjacent_bugs(point, grids):
    x, y, l = point[1], point[0], point[2]
    adjacent_points = []
    if x > 0:
        adjacent_points.append((y, x - 1, l))
    if x < 4:
        adjacent_points.append((y, x + 1, l))
    if y > 0:
        adjacent_points.append((y - 1, x, l))
    if y < 4:
        adjacent_points.append((y + 1, x, l))
    if y == 0:  # i.e. on the top border
        adjacent_points.append((1, 2, l - 1))
    elif y == 4:  # i.e on the bottom border
        adjacent_points.append((3, 2, l - 1))
    if x == 0:  # i.e. on the left border
        adjacent_points.append((2, 1, l - 1))
    elif x == 4:  # i.e. on the right border
        adjacent_points.append((2, 3, l - 1))
    elif x == 2 and y == 1:  # i.e. H
        adjacent_points.extend([(_y, _x, _l) for (_y, _x, _l) in grids.keys() if _l == l + 1 and _y == 0])
    elif x == 2 and y == 3:  # i.e. R
        adjacent_points.extend([(_y, _x, _l) for (_y, _x, _l) in grids.keys() if _l == l + 1 and _y == 4])
    elif x == 1 and y == 2:  # i.e. L
        adjacent_points.extend([(_y, _x, _l) for (_y, _x, _l) in grids.keys() if _l == l + 1 and _x == 0])
    elif x == 3 and y == 2:  # i.e. L
        adjacent_points.extend([(_y, _x, _l) for (_y, _x, _l) in grids.keys() if _l == l + 1 and _x == 4])
    if (2, 2, l) in adjacent_points:
        adjacent_points.remove((2, 2, l))
    return len([p for p in adjacent_points if p and grids.get(p, '.') == '#'])


iterations = 0
for iterations in range(200):
    levels = {k[2] for k in grids.keys()}
    die = []
    spawn = []
    for level in range(min(levels) - 1, max(levels) + 2):
        for y in range(5):
            for x in range(5):
                if not (x == 2 and y == 2):
                    recursive_adjacent = recursive_adjacent_bugs((y, x, level), grids)
                    if grids.get((y, x, level), '.') == '#' and recursive_adjacent != 1:
                        die.append((y, x, level))
                    elif grids.get((y, x, level), '.') == '.' and 0 < recursive_adjacent <= 2:
                        spawn.append((y, x, level))
    for bug in die:
        grids[bug] = '.'
    for tile in spawn:
        grids[tile] = '#'
print(len([v for (k, v) in grids.items() if v == '#']))
