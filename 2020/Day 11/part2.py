# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')

data = [[j for j in i] for i in data]


def copy(arr):
    return [[j for j in i] for i in arr]


def getNeighbors(before, i, j):
    neighbors = []

    # Find first one to the right
    for k in range(i + 1, len(before)):
        if before[k][j] != '.':
            neighbors.append(before[k][j])
            break
    # Find first one to the left
    for k in range(i - 1, -1, -1):
        if before[k][j] != '.':
            neighbors.append(before[k][j])
            break
    # Find first one below
    for k in range(j + 1, len(before[0])):
        if before[i][k] != '.':
            neighbors.append(before[i][k])
            break
    # Find first one above
    for k in range(j - 1, -1, -1):
        if before[i][k] != '.':
            neighbors.append(before[i][k])
            break

    # Up-right
    k = 1
    while i - k >= 0 and j + k < len(before[0]):
        if before[i - k][j + k] != '.':
            neighbors.append(before[i - k][j + k])
            break
        k += 1
    # Up-left
    k = 1
    while i - k >= 0 and j - k >= 0:
        if before[i - k][j - k] != '.':
            neighbors.append(before[i - k][j - k])
            break
        k += 1
    # Down-right
    k = 1
    while i + k < len(before) and j + k < len(before[0]):
        if before[i + k][j + k] != '.':
            neighbors.append(before[i + k][j + k])
            break
        k += 1
    # Down-left
    k = 1
    while i + k < len(before) and j - k >= 0:
        if before[i + k][j - k] != '.':
            neighbors.append(before[i + k][j - k])
            break
        k += 1

    return neighbors


while True:
    before = copy(data)
    changed = False
    for i in range(len(data)):
        for j in range(len(data[i])):
            if before[i][j] == '.':
                continue
            neighbors = getNeighbors(before, i, j)

            if before[i][j] == '#' and neighbors.count('#') >= 5:
                data[i][j] = 'L'
                changed = True
            if before[i][j] == 'L' and '#' not in neighbors:
                data[i][j] = '#'
                changed = True

    if not changed:
        break


print(sum([i.count('#') for i in data]))
