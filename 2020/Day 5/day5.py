import math

# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')


def getSeatID(seatData):
    lo = 0
    hi = 127
    for i in seatData[:7]:
        if i == "F":
            hi = math.ceil((hi + lo) / 2)
        else:
            lo = math.ceil((hi + lo) / 2)

    row = lo
    lo = 0
    hi = 7
    for i in seatData[7:]:
        if i == "L":
            hi = math.ceil((hi + lo) / 2)
        else:
            lo = math.ceil((hi + lo) / 2)

    col = lo
    return row * 8 + col


def part1():
    m = -1

    for person in data:
        m = max(m, getSeatID(person))

    return m


def part2():
    seen = set()
    for person in data:
        seen.add(getSeatID(person))

    print(seen)

    for i in range(32, 848):
        if i not in seen:
            return i


print(part1())
print(part2())
