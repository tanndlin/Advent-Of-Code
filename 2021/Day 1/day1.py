data = open("input.txt", "r").read().split("\n")
data = [int(x) for x in data]


def part1():
    total = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            total += 1
    return total


def part2():
    total = 0
    for i in range(3, len(data)):
        if data[i] > data[i-3]:
            total += 1
    return total


print(part1())
print(part2())
