counter_part_one = 0
counter_part_two = 0
for password in range(130254, 678275):
    ascend = all(c1 <= c2 for c1, c2 in zip(str(password), str(password)[1:]))
    if ascend:
        double = any(c1 == c2 for c1, c2 in zip(str(password), str(password)[1:]))
        if double:
            counter_part_one += 1
            if any(str(password).count(c) == 2 for c in str(password)):
                counter_part_two += 1
print(counter_part_one)
print(counter_part_two)
