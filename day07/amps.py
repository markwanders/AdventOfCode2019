with open("input.txt") as f:
    ops = [int(i) for i in f.readline().split(",")]


def run_program(phase, inp):
    mem = ops[:]
    index = 0
    while index in range(len(mem)):
        opcode = str(mem[index]).zfill(5)
        if opcode.endswith("99"):
            print("Quitting")
            break
        first = index + 1 if opcode[2] == "1" else mem[index + 1]
        second = index + 2 if opcode[1] == "1" else mem[index + 2]
        third = index + 3 if opcode[0] == "1" else mem[index + 3]
        if opcode.endswith("1"):
            mem[third] = mem[second] + mem[first]
            index += 4
        elif opcode.endswith("2"):
            mem[third] = mem[second] * mem[first]
            index += 4
        elif opcode.endswith("3"):
            mem[first] = inp if index > 0 else phase
            index += 2
        elif opcode.endswith("4"):
            return mem[first]
        elif opcode.endswith("5"):
            index = mem[second] if mem[first] != 0 else index + 3
        elif opcode.endswith("6"):
            index = mem[second] if mem[first] == 0 else index + 3
        elif opcode.endswith("7"):
            mem[third] = 1 if mem[first] < mem[second] else 0
            index += 4
        elif opcode.endswith("8"):
            mem[third] = 1 if mem[first] == mem[second] else 0
            index += 4


# part one
max_value = 0
phases = {str(i).zfill(5) for i in range(0, 44444)}
phases = {p for p in phases if (not any(p.count(c) > 1 for c in p)) and (not any(int(c) > 4 for c in p))}

for current_phase in phases:
    output = 0
    for p in current_phase:
        output = run_program(int(p), output)
    if output > max_value:
        max_value = output
        print("Max value: %d for phase %s" % (max_value, current_phase))
