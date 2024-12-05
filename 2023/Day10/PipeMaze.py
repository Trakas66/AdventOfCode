maxSteps = 0
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
upO = ["|", "F", "7"]
downO = ["|", "L", "J"]
leftO = ["-", "L", "F"]
rightO = ["-", "7", "J"]
maxV = 0

q = [start]
while len(q) > 0:
    current = q.pop(0)
    sym = maze[current[0]][current[1]]
    if current[2] > maxV:
        maxV = current[2]

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

    if down and current[0] + 1 < len(maze) and (current[0]+1, current[1]) not in explored:
        if maze[current[0]+1][current[1]] in downO:
            explored.append((current[0]+1, current[1]))
            q.append((current[0]+1, current[1], current[2]+1))

    if left and current[1] - 1 >= 0 and (current[0], current[1]-1) not in explored:
        if maze[current[0]][current[1]-1] in leftO:
            explored.append((current[0], current[1]-1))
            q.append((current[0], current[1]-1, current[2]+1))

    if right and current[1] + 1 < len(maze[0]) and (current[0], current[1]+1) not in explored:
        if maze[current[0]][current[1]+1] in rightO:
            explored.append((current[0], current[1]+1))
            q.append((current[0], current[1]+1, current[2]+1))

print(maxV)
