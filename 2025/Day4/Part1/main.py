filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

sum = 0
width = len(input[0])
height = len(input)

for i in range(height):
    for j in range(width):
        if input[i][j] != "@":
            continue
        
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
        if count < 4:
            sum += 1

print(sum)