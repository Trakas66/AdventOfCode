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

final_ranges = []
for r in ranges:
    newRange = True
    index = 0
    for j in range(len(final_ranges)):
        if newRange:
            fr = final_ranges[j]
            if r[0] <= fr[0] and r[1] >= fr[1]:
                newRange = False
                index = j
                final_ranges[j] = r
            elif r[0] <= fr[0] and r[1] >= fr[0]:
                newRange = False
                index = j
                final_ranges[j] = (r[0], fr[1])
            elif r[0] >= fr[0] and r[0] <= fr[1] and r[1] >= fr[1]:
                newRange = False
                index = j
                final_ranges[j] = (fr[0], r[1])
            elif r[0] >= fr[0] and r[1] <= fr[1]:
                newRange = False
                index = j
        else:
            r = final_ranges[index]
            fr = final_ranges[j]
            if r[0] <= fr[0] and r[1] >= fr[1]:
                final_ranges[j] = (-j,-j-1)
            elif r[0] <= fr[0] and r[1] >= fr[0]:
                final_ranges[j] = (r[1]+1, fr[1])
            elif r[0] >= fr[0] and r[0] <= fr[1] and r[1] >= fr[1]:
                final_ranges[j] = (fr[0], r[0]-1)
            elif r[0] >= fr[0] and r[1] <= fr[1]:
                final_ranges[index] = (-index,-index-1)
    if newRange:
        final_ranges.append(r)

sum = 0
for fr in final_ranges:
    sum += fr[1] - fr[0] + 1

print(sum)