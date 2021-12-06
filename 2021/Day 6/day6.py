# data = open('simple.txt', 'r').read().split(',')
data = open('input.txt', 'r').read().split(',')

data = [int(x) for x in data]
freq = {}
for i in range(9):
    freq[i] = 0

for i in data:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1


def part1(freq, days):
    for i in range(days):
        newFreq = freq.copy()
        newFreq[8] = freq[0]
        for j in range(8):
            newFreq[j] = freq[(j+1) % 9]
        newFreq[6] += freq[0]

        freq = newFreq

    total = 0
    for i in freq:
        total += freq[i]
    return total


def part2(freq):
    return part1(freq, 256)


print(part1(freq, 80))
print(part2(freq))
