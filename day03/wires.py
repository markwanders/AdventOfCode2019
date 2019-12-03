with open("input.txt") as my_file:
    wires = my_file.readline()
wires = [str(i) for i in wires.split(",")]
print(wires)
