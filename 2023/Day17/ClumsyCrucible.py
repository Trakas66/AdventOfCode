file = open(r"sample.txt")
nums = file.read().split("\n")
maze = []
for i in range(len(nums)):
    line = []
    for j in range(len(nums[0])):
        line.append(int(nums[i][j]))
    maze.append(line)

costs = [[0 for j in range(len(maze[0]))] for i in range(len(maze))]
minLen = len(maze) + len(maze[0])
found = False
count = 1
while not found:
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == count:
                costs[i][j] = count
    
