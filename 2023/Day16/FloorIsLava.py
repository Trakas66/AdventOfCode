sum = 0
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

energ = [(0,0)]
path = {}
q = [((0,0),(0,1))]
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

sum = len(energ)
print(sum)
