filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

def remove_roll(i, j, width, height, input):
    count = 0
    for k in range(-1, 2):
        for m in range(-1, 2):
            if k == 0 and m == 0:
                continue
            x, y = i+k, j+m
            if x < 0 or y < 0 or x >= height or y >= width:
                continue
            if input[x][y] == "@":
                count += 1
    if count >= 4:
        return (0, input)

    sum = 1
    input[i] = input[i][:j] + 'x' + input[i][j+1:]
    for k in range(-1, 2):
        for m in range(-1, 2):
            if k == 0 and m == 0:
                continue
            x, y = i+k, j+m
            if x < 0 or y < 0 or x >= height or y >= width:
                continue
            if input[x][y] == "@":
                num, input = remove_roll(x, y, width, height, input)
                sum += num
    return (sum, input)

sum = 0
width = len(input[0])
height = len(input)

for i in range(height):
    for j in range(width):
        if input[i][j] == "@":
            num, input = remove_roll(i, j, width, height, input)
            sum += num

print(sum)