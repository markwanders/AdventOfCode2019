from itertools import count

with open("input.txt") as f:
    ops = [int(i) for i in f.readline().split(",")]


class Computer:
    def __init__(self, code):
        self.mem = (code[:] + [0] * 10000)[:10000]
        self.index = 0
        self.relative = 0
        self.inputs = []

    def parameter_mode(self, op, param):
        if op[3 - param] == "0":
            return self.mem[self.index + param]
        elif op[3 - param] == "1":
            return self.index + param
        elif op[3 - param] == "2":
            return self.mem[self.index + param] + self.relative

    def run_program(self, inputs):
        self.inputs.append(inputs)
        while self.index in range(len(self.mem)):
            opcode = str(self.mem[self.index]).zfill(5)
            if opcode.endswith("99"):
                break
            first = self.parameter_mode(opcode, 1)
            second = self.parameter_mode(opcode, 2)
            third = self.parameter_mode(opcode, 3)
            if opcode.endswith("1"):
                self.mem[third] = self.mem[second] + self.mem[first]
                self.index += 4
            elif opcode.endswith("2"):
                self.mem[third] = self.mem[second] * self.mem[first]
                self.index += 4
            elif opcode.endswith("3"):
                self.mem[first] = inputs.pop(0)
                self.index += 2
            elif opcode.endswith("4"):
                self.index += 2
                return self.mem[first]
            elif opcode.endswith("5"):
                self.index = self.mem[second] if self.mem[first] != 0 else self.index + 3
            elif opcode.endswith("6"):
                self.index = self.mem[second] if self.mem[first] == 0 else self.index + 3
            elif opcode.endswith("7"):
                self.mem[third] = 1 if self.mem[first] < self.mem[second] else 0
                self.index += 4
            elif opcode.endswith("8"):
                self.mem[third] = 1 if self.mem[first] == self.mem[second] else 0
                self.index += 4
            elif opcode.endswith("9"):
                self.relative += self.mem[first]
                self.index += 2


grid = {}
grid_max = 50
for y in range(grid_max):
    for x in range(grid_max):
        # optional speed-ups
        if grid.get((x - 1, y), 1) == 0 and any(p == 1 for p in [grid[_x, y] for _x in range(0, x)]):
            grid[(x, y)] = 0
            continue
        if grid.get((x + 1, y - 1), 1) == 0 and any(p == 1 for p in [grid[_x, y - 1] for _x in range(x + 1, grid_max)]):
            grid[(x, y)] = 0
            continue
        drone = Computer(ops)
        grid[(x, y)] = drone.run_program([x, y])
print(sum(grid.values()))


def find_square(size):
    size -= 1
    x_start = 0
    for y in count(size):
        for x in count(x_start):
            drone = Computer(ops)
            if drone.run_program([x, y]) == 0:
                continue
            x_start = x
            drone = Computer(ops)
            if drone.run_program([x + size, y - size]) == 0:
                break
            return x, y - size


result = find_square(100)
print(result[0] * 10000 + result[1])
