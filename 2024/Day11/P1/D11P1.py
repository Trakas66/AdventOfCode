file = open(r'../day11.txt')
input = file.read().strip()
file.close()

stones = [int(stone) for stone in input.split()]
for _ in range(25):
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            stone = str(stones[i])
            length = len(stone)
            stone1 = int(stone[:int(length/2)])
            stone2 = int(stone[int(length/2):])
            stones[i] = stone1
            i += 1
            stones.insert(i, stone2)
        else:
            stones[i] *= 2024
        i += 1

print(len(stones))
