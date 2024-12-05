most = 0
grid = []

file = open(r"input.txt")
puzzle = file.read()
grid = puzzle.split("\n")

def debugPrint():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i,j) in energ:
                print("#", end="")
            else:
                print(".", end="")
        print()

def findNum(start, dxy):
    energ = [start]
    path = {}
    q = [((start),(dxy))]
    while len(q) > 0:
        panel = q.pop(0)
        current = grid[panel[0][0]][panel[0][1]]
        nextPanels = []
        if current == ".":
            nextPanels.append((panel[0][0]+panel[1][0], panel[0][1]+panel[1][1]))
        elif panel[1] in [(0,1),(0,-1)] and current == "-":
            nextPanels.append((panel[0][0]+panel[1][0], panel[0][1]+panel[1][1]))
        elif panel[1] in [(1,0),(-1,0)] and current == "|":
            nextPanels.append((panel[0][0]+panel[1][0], panel[0][1]+panel[1][1]))
        elif current == "\\":
            nextPanels.append((panel[0][0]+panel[1][1], panel[0][1]+panel[1][0]))
        elif current == "/":
            nextPanels.append((panel[0][0]-panel[1][1], panel[0][1]-panel[1][0]))
        elif current == "-":
            nextPanels.append((panel[0][0], panel[0][1]+1))
            nextPanels.append((panel[0][0], panel[0][1]-1))
        elif current == "|":
            nextPanels.append((panel[0][0]+1, panel[0][1]))
            nextPanels.append((panel[0][0]-1, panel[0][1]))

        for new in nextPanels:
            if new[0] < 0 or new[0] >= len(grid):
                continue
            if new[1] < 0 or new[1] >= len(grid[0]):
                continue
            if new in path and panel[0] in path[new]:
                continue
            if new not in energ:
                energ.append(new)
            dx = new[0]-panel[0][0]
            dy = new[1]-panel[0][1]
            q.append((new, (dx, dy)))
            if new in path:
                path[new].append(panel[0])
            else:
                path[new] = [panel[0]]

    return len(energ)

for i in range(len(grid)):
    num1 = findNum((i,0), (0,1))
    num2 = findNum((i,len(grid[0])-1), (0,-1))
    most = max([most, num1, num2])

for i in range(len(grid[0])):
    num1 = findNum((0,i), (1,0))
    num2 = findNum((len(grid)-1,i), (-1,0))
    most = max([most, num1, num2])

print(most)
