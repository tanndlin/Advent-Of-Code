# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')

data = [[int(x) for x in row] for row in data]


def check(arr, i, j, flashed):
    ret = 0

    # Ensure it stays at 0 if flashed this round
    if flashed[i][j]:
        arr[i][j] = 0

    if arr[i][j] == 10:
        arr[i][j] = 0
        flashed[i][j] = True
        ret += 1
        # increase neighbors
        if i > 0:
            arr[i-1][j] += 1
            ret += check(arr, i-1, j, flashed)

        if i < len(data)-1:
            arr[i+1][j] += 1
            ret += check(arr, i+1, j, flashed)

        if j > 0:
            arr[i][j-1] += 1
            ret += check(arr, i, j-1, flashed)

        if j < len(data[i])-1:
            arr[i][j+1] += 1
            ret += check(arr, i, j+1, flashed)

        # Diagonals
        if i > 0 and j > 0:
            arr[i-1][j-1] += 1
            ret += check(arr, i-1, j-1, flashed)

        if i > 0 and j < len(data[i])-1:
            arr[i-1][j+1] += 1
            ret += check(arr, i-1, j+1, flashed)

        if i < len(data)-1 and j > 0:
            arr[i+1][j-1] += 1
            ret += check(arr, i+1, j-1, flashed)

        if i < len(data)-1 and j < len(data[i])-1:
            arr[i+1][j+1] += 1
            ret += check(arr, i+1, j+1, flashed)

    return ret


def part1(data):
    total = 0
    for _ in range(100):
        flashed = [[False for i in row] for row in data]
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] += 1
                total += check(data, i, j, flashed)

        for i in range(len(data)):
            for j in range(len(data[i])):
                total += check(data, i, j, flashed)
    return total


def part2(data):
    times = 0
    while True:
        flashed = [[False for _ in row] for row in data]
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] += 1
                check(data, i, j, flashed)

        times += 1
        if all([all(flashed[k]) for k in range(len(data))]):
            return times


print(part1([[i for i in row] for row in data]))
print(part2(data))
