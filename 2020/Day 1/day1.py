# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')
data = [int(x) for x in data]
data = set(data)


def part1(data):
    for i in data:
        if 2020 - i in data:
            print(i * (2020 - i))
            return


# This is not supposed to be good time, time crunch lmao
def part2(data):
    data = list(data)
    sums = {}
    for i in data:
        for j in data:
            if i != j:
                sums[i + j] = (i, j)

    # Find the third number that sums to 2020
    for i in data:
        if 2020 - i in sums:
            if i not in sums[2020 - i]:
                a, b = sums[2020 - i]
                print(a, b, i)
                print(a * b * i)
                return


part1(data)
part2(data)
