with open("input.txt") as f:
    ops = [int(i) for i in f.readline().split(",")]


def run_program(inp):
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
            mem[first] = inp
            index += 2
        elif opcode.endswith("4"):
            print("Output %s" % str(mem[first]))
            index += 2
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
run_program(1)

# part two
run_program(5)
