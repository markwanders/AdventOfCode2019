from itertools import cycle
with open("input.txt") as f:
    sequence = [int(i) for i in f.readline()]

base_pattern = [0, 1, 0, -1]

output = []
input_number = sequence[0]
for index in range(len(sequence)):
    pattern = [val for val in base_pattern for _ in range(index + 1)]
    pool = cycle(pattern)
    pattern_number = next(pool)
    print(sequence[index], pattern_number)
print(output)