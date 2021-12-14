from collections import defaultdict
from typing import Counter


# data = open('simple.txt', 'r').read().split('\n\n')
data = open('input.txt', 'r').read().split('\n\n')

template, rules = data
rules = [i.split(' -> ') for i in rules.split('\n')]

conversions = {}

for i in rules:
    conversions[i[0]] = i[1]


def part1(template, steps):
    # Convert to pairs as order does not matter
    pairs = {}
    for i in conversions:
        pairs[i] = 0

    for i in range(len(template)-1):
        pairs[template[i] + template[i+1]] += 1

    for _ in range(steps):
        newFreq = pairs.copy()
        for pair in pairs:
            if pairs[pair] == 0:
                continue
            insert = conversions[pair]

            newFreq[pair[0] + insert] += pairs[pair]
            newFreq[insert + pair[1]] += pairs[pair]
            newFreq[pair] -= pairs[pair]

        pairs = newFreq

    freq = defaultdict(int)
    for i in pairs:
        freq[i[0]] += pairs[i]
        freq[i[1]] += pairs[i]

    for i in freq:
        freq[i] = freq[i] // 2

    # The ends are not double counted
    freq[template[-1]] += 1
    freq[template[0]] += 1

    # Return most common minus least common
    c = Counter(freq)
    return c.most_common()[0][1] - c.most_common()[-1][1]


print(part1(template, 10))
print(part1(template, 40))
