with open("input.txt") as f:
    ops = [int(i) for i in f.readline().split(",")]


def print_grid(grid):
    line = ""
    for _y in range(max(grid.keys())[1] + 1):
        for _x in range(max(grid.keys())[0] + 1):
            line += str(chr(grid.get((_x, _y), 46)))
        line += "\n"
    print(line)


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

    def run_program(self):
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
                self.mem[first] = self.inputs.pop(0)
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
            y += 1
            x = 0
        else:
            outputs[(x, y)] = output
            x += 1
    else:
        break

print_grid(outputs)
# part one
scaffolds = [k for (k, v) in outputs.items() if v == 35]
intersections = [s for s in scaffolds if all(elem in scaffolds for elem in adjacent(s[0], s[1]))]
print(sum(p[0] * abs(p[1]) for p in intersections))

# part two
# worked out manually:
# the path is L10R8R8L10R8R8L10L12R8R10R10L12R10L10L12R8R10R10L12R10L10L12R8R10R10L12R10R10L12R10L10R8R8
# meaning A = L10R8R8, B = L10L12R8R10, C = R10L12R10 and the path is AABCBCBCCA

move_ops = ops[:]
move_ops[0] = 2
move_robot = Computer(move_ops)
ascii_input = list(map(ord, "A,A,B,C,B,C,B,C,C,A\nL,10,R,8,R,8\nL,10,L,12,R,8,R,10\nR,10,L,12,R,10\nn\n"))
move_robot.inputs = ascii_input
part_two_output = []

while True:
    output = move_robot.run_program()
    if output:
        part_two_output.append(output)
    else:
        break

print(part_two_output[-1])
