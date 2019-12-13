# coding=utf-8

with open("input.txt") as f:
    ops = [int(i) for i in f.readline().split(",")]


def display(outputs):
    for y in range(min(map(lambda k: k[1], outputs.keys())), max(map(lambda k: k[1], outputs.keys()))):
        line = ""
        for x in range(min(map(lambda k: k[0], outputs.keys())), max(map(lambda k: k[0], outputs.keys())) + 1):
            if outputs[(x, y)] == 0:
                line += " "
            elif outputs[(x, y)] == 1:
                line += "█"
            elif outputs[(x, y)] == 2:
                line += "#"
            elif outputs[(x, y)] == 3:
                line += "_"
            elif outputs[(x, y)] == 4:
                line += "0"
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


# part one
arcade = Computer(ops)
proceed = True
outputs = {}
while proceed:
    x, y, tile_id = arcade.run_program(), arcade.run_program(), arcade.run_program()
    if x is None and y is None and tile_id is None:
        proceed = False
    else:
        outputs[(x, y)] = tile_id
print(sum(v == 2 for v in outputs.values()))


# part two
outputs = {}
arcade = Computer(ops)
arcade.mem[0] = 2
j = 0
while not outputs or any(v == 2 for v in outputs.values()):
    proceed = True
    while proceed:
        x, y, tile_id = arcade.run_program(j), arcade.run_program(j), arcade.run_program(j)
        if x is None and y is None and tile_id is None:
            proceed = False
        elif x == -1 and y == 0:
            display(outputs)
            print("Score: %d" % tile_id)
        else:
            outputs[(x, y)] = tile_id
            if any(v == 4 for v in outputs.values()) and any(v == 3 for v in outputs.values()):
                ball = [k for k, v in outputs.items() if v == 4][0]
                paddle = [k for k, v in outputs.items() if v == 3][0]

                if paddle[0] < ball[0]:
                    j = 1
                elif paddle[0] > ball[0]:
                    j = -1
                else:
                    j = 0
