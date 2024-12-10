file = open(r'../day10.txt')
input = file.readlines()
file.close()

trailMap = [line.strip() for line in input]
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def getScore(pos):
    queue = [pos]
    explored = []
    score = 0
    
    while len(queue) > 0:
        pos = queue.pop(0)
        if int(trailMap[pos[0]][pos[1]]) == 9:
            score += 1
        
        for d in directions:
            newPos = (pos[0]+d[0], pos[1]+d[1])
            if newPos in explored:
                continue
            if newPos[0] < 0 or newPos[1] < 0 or newPos[0] >= len(trailMap) or newPos[1] >= len(trailMap[0]):
                continue
            if int(trailMap[newPos[0]][newPos[1]]) - int(trailMap[pos[0]][pos[1]]) == 1:
                queue.append(newPos)
                explored.append(newPos)

    return score

trailheads = []
for i in range(len(trailMap)):
    for j in range(len(trailMap[i])):
        if int(trailMap[i][j]) == 0:
            trailheads.append((i, j))

total = 0
for head in trailheads:
    total += getScore(head)

print(total)
