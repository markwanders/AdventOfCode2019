import heapq

with open("input.txt") as f:
    raw_cave = [line.rstrip() for line in f]

cave = {}
y = 0
for _y in raw_cave:
    x = 0
    for _x in _y:
        cave[(x, y)] = _x
        x += 1
    y += 1

keys = {(k, v) for (k, v) in cave.items() if ord(v) in range(97, 123)}
collected_keys = []
print(keys)

def dijkstra(grid, origin, target):
    queue = []
    visited = {}
    heapq.heappush(queue, (origin, 0))

    while queue:

        current_node = heapq.heappop(queue)
        # if already visited with an equal or shorter distance, skip
        if current_node in visited.keys() and visited[current_node] <= current_node[1]:
            continue

        visited[current_node] = 1

        if current_node[0] == target:
            return current_node[1]

        square = grid[current_node[0]]
        if