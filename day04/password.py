counter_part_one = 0
counter_part_two = 0
for p in range(130254, 678275):
    d = any(c1 == c2 for c1, c2 in zip(str(p), str(p)[1:]))
    lt = not any(c1 > c2 for c1, c2 in zip(str(p), str(p)[1:]))
    if d and lt:
        counter_part_one += 1
        if any(str(p).count(c) == 2 for c in str(p)):
            counter_part_two += 1
print(counter_part_one)
print(counter_part_two)
