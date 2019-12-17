# coding=utf-8

with open("input.txt") as f:
    ops = [int(i) for i in f.readline().split(",")]


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

    def run_program(self, inp):
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


def new_direction(current_direction, instruction):
    if instruction == 0:
        if current_direction == "up":
            return "left"
        elif current_direction == "down":
            return "right"
        elif current_direction == "left":
            return "down"
        elif current_direction == "right":
            return "up"
    elif instruction == 1:
        if current_direction == "up":
            return "right"
        elif current_direction == "down":
            return "left"
        elif current_direction == "left":
            return "up"
        elif current_direction == "right":
            return "down"


def paint(start):
    robot = Computer(ops)
    proceed = True
    position = (0, 0)
    squares = {position: start}
    directions = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    direction = "up"
    while proceed:
        current_color = squares[position] if position in squares.keys() else 0
        color, direction_instruction = robot.run_program(current_color), robot.run_program(current_color)
        if color is None and direction_instruction is None:
            proceed = False
        else:
            squares[position] = color
            direction = new_direction(direction, direction_instruction)
            position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
    return squares


# part one
print(len(paint(0)))

painted = paint(1)
# part two
for _y in range(max(painted.keys(), key=lambda k: k[1])[1], min(painted.keys(), key=lambda k: k[1])[1] - 1, -1):
    line = ""
    for _x in range(min(painted.keys(), key=lambda k: k[0])[0], max(painted.keys(), key=lambda k: k[0])[0]):
        pixel = painted[(_x, _y)] if (_x, _y) in painted.keys() else 0
        if pixel == 0:
            line += "  "
        if pixel == 1:
            line += "██"
    print(line)
