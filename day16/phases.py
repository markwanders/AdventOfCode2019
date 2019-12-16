from itertools import cycle, islice

with open("input.txt") as f:
    sequence = [int(i) for i in f.readline()]

base_pattern = [0, 1, 0, -1]


def fft(input_sequence):
    for p in range(0, 100):
        output = []
        for index in range(len(input_sequence)):
            pattern = list(islice(cycle([val for val in base_pattern for _ in range(index + 1)]), len(input_sequence) + 1))[1:]
            number = abs(sum([a * b for a, b in zip(input_sequence, pattern)])) % 10
            output.append(number)
        input_sequence = output
    return input_sequence


# part one
print ''.join(map(str, fft(sequence)[:8]))

# part two
offset = num = int(''.join(map(str, sequence[:7])))
print ''.join(map(str, fft(sequence * 10000)[offset:8 + offset]))
