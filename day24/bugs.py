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
