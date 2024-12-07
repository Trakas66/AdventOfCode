file = open(r'../day6.txt')
input = file.readlines()
file.close()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def checkForLoop(start, floor):
    #temporarily add our walls hit to new array
    tempHit = []

    pos = start
    d = directions[0]
    
    #keep checking until we hit a wall the same way we have before or we leave the map
    while 1:
        nextPos = (pos[0] + d[0], pos[1] + d[1])
        if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= len(floor) or nextPos[1] >= len(floor[0]):
            return False
        if (nextPos, d) in tempHit:
            return True
        if floor[nextPos[0]][nextPos[1]] == '#':
            tempHit.append((nextPos, d))
            dirIndex = directions.index(d)
            d = directions[(dirIndex+1)%4]
        else:
            pos = nextPos

#get maze, list of walls, and start pos
floor = []
start = (0, 0)
for i in range(len(input)):
    floor.append([])
    input[i] = input[i].strip()
    for j in range(len(input[i])):
        floor[i].append(input[i][j])
        if input[i][j] == '^':
            start = (i, j)

#place a wall in every valid location and check for a loop
total = 0
for i in range(len(floor)):
    for j in range(len(floor[i])):
        if floor[i][j] == '.':
            floor[i][j] = '#'
            if checkForLoop(start, floor):
                total += 1
            floor[i][j] = '.'

print(total)
