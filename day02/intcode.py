with open("input.txt") as my_file:
    intcodes = my_file.readline()
intcodes = [int(i) for i in intcodes.split(",")]


def run_program(mem):
    for index in range(len(mem)):
        if index % 4 == 0:
            if mem[index] == 1:
                mem[mem[index + 3]] = mem[mem[index + 1]] + mem[mem[index + 2]]
            elif mem[index] == 2:
                mem[mem[index + 3]] = mem[mem[index + 1]] * mem[mem[index + 2]]
            elif mem[index] == 99:
                return
            else:
                print("Encountered unknown opcode " + str(mem[index]) + ", quitting")
                return


# part 1
memory = intcodes[:]
memory[1] = 12
memory[2] = 2
run_program(memory)
print(memory[0])

# part 2
for noun in range(0, 100):
    for verb in range(0, 100):
        memory = intcodes[:]
        memory[1] = noun
        memory[2] = verb
        run_program(memory)
        if memory[0] == 19690720:
            print("Found required value at 100 * noun + verb = " + str(100 * noun + verb))
            break
