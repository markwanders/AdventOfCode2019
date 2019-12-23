with open("input.txt") as f:
    ops = [int(i) for i in f.readline().split(",")]

packets = {a: [a] for a in range(50)}
packets[255] = []


class Computer:
    def __init__(self, code, address):
        self.mem = (code[:] + [0] * 10000)[:10000]
        self.index = 0
        self.relative = 0
        self.address = address
        self.output = []

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
                if not packets[self.address]:
                    self.mem[first] = -1
                else:
                    self.mem[first] = packets[self.address].pop(0)
                self.index += 2
                break
            elif opcode.endswith("4"):
                self.index += 2
                self.output += [self.mem[first]]
                if len(self.output) == 3:
                    packets[self.output[0]] += self.output[1:3]
                    self.output = self.output[3:]
                    break
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


computers = [Computer(ops, a) for a in range(50)]
while not packets[255]:
    for computer in computers:
        computer.run_program()
print(packets[255])