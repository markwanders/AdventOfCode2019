with open("input.txt") as f:
    ops = [int(i) for i in f.readline().split(",")]


def print_grid(grid):
    line = ""
    for _y in range(0, min(grid.keys())[1], -1):
        for _x in range(max(grid.keys())[0]):
            if (_x, _y) in grid.keys():
                c = grid[(_x, _y)]
            else:
                c = 0
            if c == 35:
                line += "#"
            elif c == 46:
                line += "."
            else:
                line += " "
        line += "\n"
    print(line)


class Computer:
    def __init__(self, code):
        self.mem = (code[:] + [0] * 10000)[:10000]
        self.index = 0
        self.relative = 0

    def parameter_mode(self, op, param):
        if op[3 - param] == "0":
            return self.mem[self.index + param]
        elif op[3 - param] == "1":
            return self.index + param
        elif op[3 - param] == "2":
            return self.mem[self.index + param] + self.relative

    def run_program(self, inp=0):
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
                self.mem[first] = inp
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


def adjacent(xx, yy):
    return [(xx + 1, yy), (xx - 1, yy), (xx, yy + 1), (xx, yy - 1)]


robot = Computer(ops)
outputs = {}
x = y = 0
while True:
    output = robot.run_program()
    if output:
        if output == 10:
            y -= 1
            x = 0
        else:
            outputs[(x, y)] = output
            x += 1
    else:
        break

print_grid(outputs)
scaffolds = [k for (k, v) in outputs.items() if v == 35]
intersections = [s for s in scaffolds if all(elem in scaffolds for elem in adjacent(s[0], s[1]))]
print(sum(p[0] * abs(p[1]) for p in intersections))



