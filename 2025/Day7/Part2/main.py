filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

start_pos = 0
for i in range(len(input[0])):
    if input[0][i] == 'S':
        start_pos = i
        break

beams = {i: 0 for i in range(len(input[0]))}
beams[start_pos] = 1
for row in range(len(input)-1):
    for i in beams:
        if beams[i] == 0:
            continue
        elif input[row+1][i] == '^':
            num = beams[i]
            beams[i] = 0
            beams[i-1] += num
            beams[i+1] += num

splits = 0
for i in beams:
    splits += beams[i]

print(splits)