file = open(r'../day6.txt')
input = file.readlines()
file.close()

#get maze and start pos
floor = []
start = (0, 0)
for i in range(len(input)):
    floor.append([])
    input[i] = input[i].strip()
    for j in range(len(input[i])):
        floor[i].append(input[i][j])
        if input[i][j] == '^':
            start = (i, j)

#walk through maze until off the grid
pos = [start[0], start[1]]
d = [-1, 0]
visited = [pos]
while 1:
    nextPos = [pos[0] + d[0], pos[1] + d[1]]
    if nextPos[0] < 0 or nextPos[0] >= len(floor) or nextPos[1] < 0 or nextPos[1] >= len(floor[0]):
        break
    if floor[nextPos[0]][nextPos[1]] == '#':
        #turn right
        if d[0] != 0:
            d[1] = d[0] * -1
            d[0] = 0
        else:
            d[0] = d[1]
            d[1] = 0
    else:
        #go forward one space
        pos = nextPos
        if not pos in visited:
            visited.append(pos)

print(len(visited))
