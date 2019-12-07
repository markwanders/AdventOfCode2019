with open("input.txt") as f:
    ops = [int(i) for i in f.readline().split(",")]


class Amplifier:
    def __init__(self, code):
        self.mem = code[:]
        self.index = 0

    def run_program(self, inputs):
        while self.index in range(len(self.mem)):
            opcode = str(self.mem[self.index]).zfill(5)
            if opcode.endswith("99"):
                break
            first = self.index + 1 if opcode[2] == "1" else self.mem[self.index + 1]
            second = self.index + 2 if opcode[1] == "1" else self.mem[self.index + 2]
            if opcode.endswith(("1", "2", "7", "8")):
                third = self.index + 3 if opcode[0] == "1" else self.mem[self.index + 3]
            else:
                third = 0
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


# part one
phases = {str(i).zfill(5) for i in range(0, 44444)}
phases = {p for p in phases if (not any(p.count(c) > 1 for c in p)) and (not any(int(c) > 4 for c in p))}
outputs = []
for current_phase in phases:
    output = 0
    amplifiers = [Amplifier(ops) for _ in range(5)]
    for amplifier, phase in zip(amplifiers, current_phase):
        output = amplifier.run_program(inputs=[int(phase), output])
    outputs.append(output)
print(max(outputs))

# part two
phases = {str(i).zfill(5) for i in range(55555, 99999)}
phases = {p for p in phases if (not any(p.count(c) > 1 for c in p)) and (not any(int(c) < 5 for c in p))}
for current_phase in phases:
    amplifiers = [Amplifier(ops) for _ in range(5)]

    output = 0
    for amplifier, phase in zip(amplifiers, current_phase):
        output = amplifier.run_program(inputs=[int(phase), output])

    while True:
        for amplifier in amplifiers:
            output = amplifier.run_program(inputs=[output])

        if output:
            outputs.append(output)
        else:
            break
print(max(outputs))
