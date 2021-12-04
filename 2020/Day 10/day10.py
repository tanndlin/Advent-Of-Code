data = open('simple.txt', 'r').read().split('\n')
# data = open('input.txt', 'r').read().split('\n')

data = [int(i) for i in data]
data.sort()


def part1():
    diff = {1: 1, 2: 0, 3: 1}

    for i in range(len(data)-1):
        diff[data[i+1] - data[i]] += 1
    return diff[1] * diff[3]


print(part1())
