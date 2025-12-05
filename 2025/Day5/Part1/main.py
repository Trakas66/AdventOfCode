filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

ranges = []
i = 0
while input[i] != "":
    newRange = input[i].split("-")
    newRange = (int(newRange[0]), int(newRange[1]))
    ranges.append(newRange)
    i += 1

length = len(input)
sum = 0
for j in range(i+1, length):
    num = int(input[j])
    valid = False
    for r in ranges:
        if num >= r[0] and num <= r[1]:
            valid = True
            break
    if valid:
        sum += 1

print(sum)