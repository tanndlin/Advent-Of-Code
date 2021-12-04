# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')


def part1(sequence):
    acc = 0

    i = 0
    seen = set()
    while True:
        if i >= len(sequence):
            return acc

        if i in seen:
            return acc
        seen.add(i)

        if 'nop' in sequence[i]:
            i += 1
        elif 'acc' in sequence[i]:
            acc += int(sequence[i].split(' ')[1])
            i += 1
        elif 'jmp' in sequence[i]:
            i += int(sequence[i].split(' ')[1])


def part2():
    def terminates(sequence):
        seen = set()
        i = 0
        while i < len(sequence):
            if i in seen:
                return False

            seen.add(i)
            if 'nop' in sequence[i] or 'acc' in sequence[i]:
                i += 1
            elif 'jmp' in sequence[i]:
                i += int(sequence[i].split(' ')[1])

        return True

    for i in range(len(data)):
        if 'nop' in data[i]:
            newData = data.copy()
            newData[i] = newData[i].replace('nop', 'jmp')
            if terminates(newData):
                return part1(newData)
        if 'jmp' in data[i]:
            newData = data.copy()
            newData[i] = newData[i].replace('jmp', 'nop')
            if terminates(newData):
                return part1(newData)

    return -1


print(part1(data))
print(part2())
