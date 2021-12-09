import time

# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')


def getNeighbors(i, j):
    neighbors = []
    if i > 0:
        neighbors.append((i-1, j))
    if i < len(data)-1:
        neighbors.append((i+1, j))
    if j > 0:
        neighbors.append((i, j-1))
    if j < len(data[i])-1:
        neighbors.append((i, j+1))

    return neighbors


def getSizeOfBasin(i, j):
    visited = set((i, j))
    total = 0

    stack = []
    stack.append((i, j))

    while stack:
        i, j = stack.pop()
        if (i, j) in visited:
            continue

        total += 1
        visited.add((i, j))

        for nI, nJ in getNeighbors(i, j):
            # Basins are the area surrounded by 9's as 9's cannot be apart of a basin
            if int(data[nI][nJ]) != 9 and (nI, nJ) not in visited:
                stack.append((nI, nJ))
    return total


def part1():
    lows = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            neighbors = getNeighbors(i, j)

            # Check if lower than all neighbors
            if all([data[i][j] < data[k][l] for k, l in neighbors]):
                lows.append((i, j))
    return lows


def part2():
    lows = part1()
    basins = [getSizeOfBasin(i, j) for i, j in lows]

    basins.sort()
    print(basins)
    return basins[-1] * basins[-2] * basins[-3]


start_time = time.time()
lows = part1()
print(sum([int(data[i][j]) for i, j in lows]) + len(lows))
print(part2())
print("--- %s ms ---" % ((time.time() - start_time) * 1000))
