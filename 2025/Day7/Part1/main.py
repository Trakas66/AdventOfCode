filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

start_pos = 0
for i in range(len(input[0])):
    if input[0][i] == 'S':
        start_pos = i
        break

beams = [start_pos]
splits = 0
for row in range(len(input)-1):
    new_beams = []
    for beam in beams:
        if input[row+1][beam] == '.':
            new_beams.append(beam)
        elif input[row+1][beam] == "^":
            new_beams.append(beam-1)
            new_beams.append(beam+1)
            splits += 1
    beams = list(set(new_beams))

print(splits)