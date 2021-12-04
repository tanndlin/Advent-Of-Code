# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')


def part1(slopeX, slopeY):
    count = 0
    x = 0
    y = 0

    while y < len(data)-1:
        x += slopeX
        y += slopeY

        if data[y][x % len(data[0])] == '#':
            count += 1
    return count


def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    count = 1
    for slope in slopes:
        count *= part1(slope[0], slope[1])
    return count


print(part1(3, 1))
print(part2())
