from itertools import cycle, islice

with open("input.txt") as f:
    sequence = [int(i) for i in f.readline()]

base_pattern = [0, 1, 0, -1]

for p in range(0, 100):
    output = []
    for index in range(len(sequence)):
        pattern = list(islice(cycle([val for val in base_pattern for _ in range(index + 1)]), len(sequence) + 1))[1:]
        number = abs(sum([a * b for a, b in zip(sequence, pattern)])) % 10
        output.append(number)
    sequence = output
print ''.join(map(str, sequence[:8]))
