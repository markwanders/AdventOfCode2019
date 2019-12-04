counter = 0
for p in range(130254, 678275):
    ints = [int(i) for i in str(p)]
    d = False
    lt = False
    for i in range(1, 6):
        if ints[i] == ints[i - 1]:
            d = True
        if ints[i] >= ints[i - 1]:
            lt = True
        else:
            lt = False
            break
    if d and lt:
        counter = counter + 1
print(counter)
