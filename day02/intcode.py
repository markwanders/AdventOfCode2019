with open("input.txt") as f:
    intcodes = [int(i) for i in f.readline().split(",")]


def run_program(mem):
    for index in range(len(mem)):
        if index % 4 == 0:
            if mem[index] == 1:
                mem[mem[index + 3]] = mem[mem[index + 1]] + mem[mem[index + 2]]
            elif mem[index] == 2:
                mem[mem[index + 3]] = mem[mem[index + 1]] * mem[mem[index + 2]]
            elif mem[index] == 99:
                break
            else:
                print("Encountered unknown opcode " + str(mem[index]) + ", quitting")
                break
    return mem[0]


# part 1
memory = intcodes[:]
memory[1] = 12
memory[2] = 2
print(run_program(memory))

# part 2
for noun in range(100):
    for verb in range(100):
        memory = intcodes[:]
        memory[1] = noun
        memory[2] = verb
        if run_program(memory) == 19690720:
            print("Found required value at 100 * noun + verb = " + str(100 * noun + verb))
            break
