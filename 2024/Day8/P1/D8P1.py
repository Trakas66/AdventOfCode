file = open(r'../day8.txt')
input = file.readlines()
file.close()

locs = [line.strip() for line in input]
antennae = {}
antinodes = []

for i in range(len(locs)):
    for j in range(len(locs[i])):
        if locs[i][j] != '.':
            if locs[i][j] in antennae:
                antennae[locs[i][j]].append((i, j))
            else:
                antennae[locs[i][j]] = [(i, j)]

for key in antennae:
    value = antennae[key]
    for i in range(len(value)):
        for j in range(i+1, len(value)):
            diff = (value[j][0]-value[i][0], value[j][1]-value[i][1])
            loc1 = (value[j][0]+diff[0], value[j][1]+diff[1])
            loc2 = (value[i][0]-diff[0], value[i][1]-diff[1])

            if loc1 not in antinodes:
                if loc1[0] >= 0 and loc1[0] < len(locs) and loc1[1] >= 0 and loc1[1] < len(locs[0]):
                    antinodes.append(loc1)
            if loc2 not in antinodes:
                if loc2[0] >= 0 and loc2[0] < len(locs) and loc2[1] >= 0 and loc2[1] < len(locs[0]):
                    antinodes.append(loc2)

print(len(antinodes))
