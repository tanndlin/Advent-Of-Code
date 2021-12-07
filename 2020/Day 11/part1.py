# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')

data = [[j for j in i] for i in data]


def copy(arr):
    return [[j for j in i] for i in arr]


def part1():
    while True:
        changed = False
        before = copy(data)
        for i in range(len(before)):
            for j in range(len(before[i])):
                neighbors = []
                if i > 0:
                    neighbors.append(before[i-1][j])
                if i < len(before)-1:
                    neighbors.append(before[i+1][j])
                if j > 0:
                    neighbors.append(before[i][j-1])
                if j < len(before[i])-1:
                    neighbors.append(before[i][j+1])
                if i > 0 and j > 0:
                    neighbors.append(before[i-1][j-1])
                if i > 0 and j < len(before[i])-1:
                    neighbors.append(before[i-1][j+1])
                if i < len(before)-1 and j > 0:
                    neighbors.append(before[i+1][j-1])
                if i < len(before)-1 and j < len(before[i])-1:
                    neighbors.append(before[i+1][j+1])

                if before[i][j] == 'L' and neighbors.count('#') == 0:
                    changed = True
                    data[i][j] = '#'
                if before[i][j] == '#' and neighbors.count('#') >= 4:
                    changed = True
                    data[i][j] = 'L'
        if not changed:
            break
    return sum([i.count('#') for i in data])


print(part1())
