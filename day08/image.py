with open("input.txt") as f:
    image = [char for char in str(f.readline())]

x, y = 25, 6

layers = [image[i:i + (x * y)] for i in range(0, len(image), (x * y))]

# part one
min_zeroes = min(layers, key=lambda layer: layer.count('0'))
part_one = min_zeroes.count('1') * min_zeroes.count('2')
print(part_one)

# part two
for _y in range(y):
    line = ""
    for _x in range(x):
        pixel_nr = (_y * x) + _x
        pixels = [layer[pixel_nr] for layer in layers]
        for pixel in pixels:
            if pixel == "0":
                line += ".."
                break
            if pixel == "1":
                line += "##"
                break
    print(line)
