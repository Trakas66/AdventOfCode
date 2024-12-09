file = open(r'../day8.txt')
input = file.readlines()
file.close()

locs = [line.strip() for line in input]
antennae = {}
antinodes = set()

for i in range(len(locs)):
    for j in range(len(locs[i])):
        if locs[i][j] != '.':
            if locs[i][j] in antennae:
                antennae[locs[i][j]].append((i, j))
            else:
                antennae[locs[i][j]] = [(i, j)]

for i in range(len(locs)):
    for j in range(len(locs[i])):
        for key in antennae:
            value = antennae[key]
            if len(value) == 1:
                continue
            for k in range(len(value)):
                for l in range(k+1, len(value)):
                    diff = (value[l][0]-value[k][0], value[l][1]-value[k][1])
                    loc = (value[l][0] - i, value[l][1] - j)
                    if (i, j) == value[l]:
                        antinodes.add((i, j))
                    elif loc[1] == 0:
                        if diff[1] == 0:
                            antinodes.add((i, j))
                    elif diff[1] == 0:
                        continue
                    elif loc[0]/loc[1] == diff[0]/diff[1]:
                        antinodes.add((i, j))

print(len(antinodes))
