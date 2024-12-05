sum = 0
maze = []

while 1:
    line = input()
    if line == "":
        break
    maze.append(line)

start = 0

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            start = (i, j, 0)

if start == 0:
    print("Start not found")

explored = []
path = {}
upO = ["|", "F", "7"]
downO = ["|", "L", "J"]
leftO = ["-", "L", "F"]
rightO = ["-", "7", "J"]
maxV = 0
maxPos = (0, 0)

q = [start]
while len(q) > 0:
    current = q.pop(0)
    sym = maze[current[0]][current[1]]
    if current[2] > maxV:
        maxV = current[2]
        maxPos = (current[0], current[1])

    up = down = left = right = False

    if current == start:
        up = down = left = right = True
    elif sym == "|":
        up = down = True
    elif sym == "-":
        left = right = True
    elif sym == "F":
        right = down = True
    elif sym == "J":
        left = up = True
    elif sym == "7":
        left = down = True
    elif sym == "L":
        right = up = True

    if up and current[0] - 1 >= 0 and (current[0]-1, current[1]) not in explored:
        if maze[current[0]-1][current[1]] in upO:
            explored.append((current[0]-1, current[1]))
            q.append((current[0]-1, current[1], current[2]+1))
            path[(current[0]-1, current[1])] = (current[0], current[1])

    if down and current[0] + 1 < len(maze) and (current[0]+1, current[1]) not in explored:
        if maze[current[0]+1][current[1]] in downO:
            explored.append((current[0]+1, current[1]))
            q.append((current[0]+1, current[1], current[2]+1))
            path[(current[0]+1, current[1])] = (current[0], current[1])

    if left and current[1] - 1 >= 0 and (current[0], current[1]-1) not in explored:
        if maze[current[0]][current[1]-1] in leftO:
            explored.append((current[0], current[1]-1))
            q.append((current[0], current[1]-1, current[2]+1))
            path[(current[0], current[1]-1)] = (current[0], current[1])

    if right and current[1] + 1 < len(maze[0]) and (current[0], current[1]+1) not in explored:
        if maze[current[0]][current[1]+1] in rightO:
            explored.append((current[0], current[1]+1))
            q.append((current[0], current[1]+1, current[2]+1))
            path[(current[0], current[1]+1)] = (current[0], current[1])


def testPrint(myList):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i,j) in myList:
                print(maze[i][j], end="")
            else:
                print(" ", end="")
        print()


loop = []
current = maxPos

while current in path:
    loop.append(current)
    current = path[current]
loop.append((start[0], start[1]))

up = down = left = right = True
checked = path[maxPos]
if checked[0] < maxPos[0]:
    up = False
if checked[0] > maxPos[0]:
    down = False
if checked[1] < maxPos[1]:
    left = False
if checked[1] > maxPos[1]:
    right = False

new = (0,0)
if up and maxPos[0]-1 >= 0 and maze[maxPos[0]-1][maxPos[1]] in upO:
    new = (maxPos[0]-1, maxPos[1])
elif down and maxPos[0]+1 < len(maze) and maze[maxPos[0]+1][maxPos[1]] in downO:
    new = (maxPos[0]+1, maxPos[1])
elif left and maxPos[1]-1 >= 0 and maze[maxPos[0]][maxPos[1]-1] in leftO:
    new = (maxPos[0], maxPos[1]-1)
elif right and maxPOs[1]+1 < len(maze) and maze[maxPos[0]][maxPos[1]+1] in rightO:
    new = (maxPos[0], maxPos[1]+1)

l = []
current = new
while current in path:
    l.append(current)
    current = path[current]

for i in range(len(l)-1, -1, -1):
    loop.append(l[i])

#testPrint(loop)

#shoelace algorithm
vertices = []
for i in range(len(loop)):
    if maze[loop[i][0]][loop[i][1]] not in ["|", "-"]:
        vertices.append(loop[i])

area = 0
for i in range(len(vertices)):
    if i == len(vertices)-1:
        first = vertices[i][0]*vertices[0][1]
        second = vertices[0][0]*vertices[i][1]
        area += (first - second)
    else:
        first = vertices[i][0]*vertices[i+1][1]
        second = vertices[i+1][0]*vertices[i][1]
        area += (first-second)
area = int(abs(area/2))

#Pick's theorem
b = len(loop)
area += 1
area -= int(b/2)
print(area)
