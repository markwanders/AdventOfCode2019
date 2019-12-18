from queue import Queue

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

robot = [k for (k, v) in cave.items() if v == '@'][0]
keys = {v for (k, v) in cave.items() if ord(v) in range(97, 123)}

q = Queue()
q.put((robot, [], 0))
visited = {(robot, tuple())}

while True:
    robot, found_keys, steps = q.get()
    found_keys = set(found_keys)
    if found_keys == keys:
        print("All keys found!")
        break
    neighbors = [(robot[0] - 1, robot[1]), (robot[0] + 1, robot[1]), (robot[0], robot[1] - 1), (robot[0], robot[1] + 1)]
    for neighbor in neighbors:
        tile = str(cave[neighbor])
        if tile != '#':
            if not ('A' <= tile <= 'Z' and tile.lower() not in found_keys):  # i.e. either an open spot or an open door
                found_keys_for_node = found_keys
                if 'a' <= tile <= 'z' and tile not in found_keys_for_node:  # i.e. this is a new key
                    found_keys_for_node = found_keys_for_node | {tile}
                node = (neighbor, tuple(sorted(found_keys_for_node)))
                if node not in visited:
                    visited.add(node)
                    q.put((neighbor, node[1], steps + 1))

print(steps)