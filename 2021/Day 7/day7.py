import time
import numpy as np
# data = open('simple.txt', 'r').read().split(',')
data = open('input.txt', 'r').read().split(',')
data = [int(x) for x in data]


def go(compareFunc):
    m = float("inf")
    avg = int(np.average(data))

    i = avg
    direction = 1
    swapped = False

    while True:
        cost = 0
        for j in range(len(data)):
            if i != j:
                cost += compareFunc(i, data[j])
        if cost < m:
            m = cost
        elif cost > m:
            if swapped:
                return m
            else:
                swapped = True
                direction *= -1
        i += direction

    return m


def part1():
    def score(x, y):
        return abs(x-y)
    return go(score)


def part2():
    def score(x, y):
        n = abs(x-y)
        return n * (n + 1) // 2
    return go(score)


# Get run time
start_time = time.time()
print(part1())
print(part2())
print("--- %s ms ---" % ((time.time() - start_time) * 1000))


# 3ms
