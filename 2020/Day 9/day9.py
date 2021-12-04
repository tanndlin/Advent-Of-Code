# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')

data = [int(x) for x in data]


def part1():
    def sums(arr):
        ret = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                ret.append(arr[i] + arr[j])

        return ret

    for i in range(25, len(data)):
        if data[i] not in sums(data[i-25:i]):
            return data[i]


def part2():
    target = part1()
    for i in range(len(data)):

        j = i + 1
        total = data[i] + data[j]
        while j < len(data) and total < target:
            j += 1
            total += data[j]

        if total == target:
            return min(data[i:j+1]) + max(data[i:j+1])


print(part1())
print(part2())
