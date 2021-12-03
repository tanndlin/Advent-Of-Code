# data = open("simple.txt", 'r').read().split('\n')
data = open("input.txt", 'r').read().split('\n')


def getFreq(data, bit):
    freq = {}
    for j in data:
        first = j[bit]
        if first in freq:
            freq[first] += 1
        else:
            freq[first] = 1
    return freq


def getWinner(freq, onTie):
    winner = -1
    if freq["1"] > freq["0"]:
        winner = "1"
    elif freq["0"] > freq["1"]:
        winner = "0"
    else:
        winner = onTie

    return winner


def part1():
    gamma = ""
    eps = ""

    for i in range(len(data[0])):
        freq = getFreq(data, i)
        winner = getWinner(freq, "1")

        gamma += winner
        eps += "0" if winner == "1" else "1"

    gamma = int(gamma, 2)
    eps = int(eps, 2)
    print(gamma, eps, gamma * eps)


def part2():
    dataLeft = data.copy()
    bit = 0
    while len(dataLeft) > 1:
        freq = getFreq(dataLeft, bit)
        winner = getWinner(freq, "1")

        dataLeft = [i for i in dataLeft if i[bit] == winner]
        bit += 1

    o2 = dataLeft[0]

    dataLeft = data.copy()
    bit = 0
    while len(dataLeft) > 1:
        freq = getFreq(dataLeft, bit)

        winner = -1
        if freq["1"] < freq["0"]:
            winner = "1"
        elif freq["0"] < freq["1"]:
            winner = "0"
        else:
            winner = "0"

        dataLeft = [i for i in dataLeft if i[bit] == winner]
        bit += 1

    c02 = dataLeft[0]

    o2 = int(o2, 2)
    c02 = int(c02, 2)
    print(o2, c02, o2 * c02)


part1()
part2()
