from itertools import cycle, islice

with open("input.txt") as f:
    sequence = [int(i) for i in f.readline()]

base_pattern = [0, 1, 0, -1]


def fft(input_sequence):
    for _ in range(100):
        output = []
        for index in range(len(input_sequence)):
            pattern = list(islice(cycle([val for val in base_pattern for _ in range(index + 1)]), len(input_sequence) + 1))[1:]
            number = abs(sum([a * b for a, b in zip(input_sequence, pattern)])) % 10
            output.append(number)
        input_sequence = output
    return input_sequence


# part one
print(''.join(map(str, fft(sequence)[:8])))

# part two
# using the fact that for any sequence of length n, we know that for the final number, the phase is 0,...,0,1,
# and so the phase shifted final number s'[n] = 1 * s[n], and for the second to last number the phase is 0,...0,1,1
# (this is because our offset places us far beyond the halfway point of the sequence, and so we don't encounter -1!)
# and thus s'[n-1] = (s[n-1] + s'[n]) % 10 = (s[n-1] + s[n]) % 10, we can just count backwards from the end
offset = num = int(''.join(map(str, sequence[:7])))
sequence = (sequence * 10000)[offset:]
for _ in range(100):
    for n in range(-2, -len(sequence) - 1, -1):
        sequence[n] = (sequence[n] + sequence[n + 1]) % 10
print(''.join(map(str, sequence[:8])))
