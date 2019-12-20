from queue import Queue

with open("input.txt") as f:
    raw_torus = [line.rstrip() for line in f]

torus = {}
warps = {}
y = 0
for _y in raw_torus:
    x = 0
    for _x in _y:
        torus[(x, y)] = _x
        if 'A' <= _x <= 'Z':
            if x - 1 >= 0 and 'A' <= torus[(x - 1, y)] <= 'Z':
                warp = torus[(x - 1, y)] + _x
                if (x - 2, y) in torus.keys() and torus[(x - 2, y)] == '.':
                    warp_point = (x - 2, y)
                else:
                    warp_point = (x + 1, y)
                warps[warp_point] = warp
            if (x, y - 1) in torus.keys() and 'A' <= torus[(x, y - 1)] <= 'Z':
                warp = torus[(x, y - 1)] + _x
                if(x, y - 2) in torus.keys() and torus[(x, y - 2)] == '.':
                    warp_point = (x, y - 2)
                else:
                    warp_point = (x, y + 1)
                warps[warp_point] = warp
        x += 1
    y += 1

warp_to_warp = {k: k2 for (k, v) in warps.items() for (k2, v2) in warps.items() if v == v2 and k2 != k}
target = [k for (k, v) in warps.items() if v == 'ZZ'][0]
origin = [k for (k, v) in warps.items() if v == 'AA'][0]

# part one
q = Queue()
q.put((origin, 0))
visited = [origin]

while True:
    p, steps = q.get()
    if p == target:
        break
    neighbors = [(p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)]
    for neighbor in neighbors:
        tile = torus.get(neighbor, '#')
        if tile == '.':
            if neighbor in warp_to_warp.keys() and warp_to_warp[neighbor] not in visited:
                q.put((warp_to_warp[neighbor], steps + 2))
            if neighbor not in visited:
                visited.append(neighbor)
                q.put((neighbor, steps + 1))


print(steps)