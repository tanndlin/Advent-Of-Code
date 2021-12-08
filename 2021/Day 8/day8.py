# This code is dogshit, but in fairness so is this problem
# It's like 5% a coding problem and 95% a cognitive problem


# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')


def getWordDictFromInput(inputData):
    numToWord = {}
    for word in inputData.split(' '):
        if len(word) == 2:
            numToWord[1] = set(word)
        if len(word) == 4:
            numToWord[4] = set(word)
        if len(word) == 3:
            numToWord[7] = set(word)
        if len(word) == 7:
            numToWord[8] = set(word)

    middle = numToWord[4] - numToWord[1] - numToWord[7]
    bottomLeft = numToWord[8] - numToWord[1] - numToWord[4] - numToWord[7]

    # Find the 0 and 6
    for word in inputData.split(' '):
        if len(word) == 6 and [i in word for i in middle].count(True) == 1:
            numToWord[0] = set(word)
        if len(word) == 6 and all([i in word for i in bottomLeft]) and all([i in word for i in middle]):
            numToWord[6] = set(word)

    temp = middle
    middle = numToWord[8] - numToWord[0]
    topLeft = list(temp - middle)[0]
    topRight = list(numToWord[8] - numToWord[6])[0]
    bottomRight = list(numToWord[1] & numToWord[6])[0]

    # Find the 2 and 5
    for word in inputData.split(' '):
        if len(word) == 5 and bottomRight not in word and topLeft not in word:
            numToWord[2] = set(word)

        if len(word) == 5 and [i in word for i in bottomLeft].count(True) == 1 and topRight not in word:
            numToWord[5] = set(word)

    bottom = list(numToWord[5] & bottomLeft)[0]
    bottomLeft = list(bottomLeft - set(bottom))[0]

    # Find the 3 and 9
    for word in inputData.split(' '):
        if len(word) == 5 and topLeft not in word and bottomLeft not in word:
            numToWord[3] = set(word)
        if len(word) == 6 and bottomLeft not in word:
            numToWord[9] = set(word)

    return numToWord


def part1():
    freq = {1: 0, 4: 0, 7: 0, 8: 0}
    for row in data:
        outputs = row.split('| ')[1]
        words = outputs.split(' ')
        for i in words:
            used = set()
            for j in i:
                used.add(j)

            if len(used) == 2:
                freq[1] += 1
            if len(used) == 4:
                freq[4] += 1
            if len(used) == 3:
                freq[7] += 1
            if len(used) == 7:
                freq[8] += 1

    total = 0
    for i in freq:
        total += freq[i]
    return total


def part2():
    ret = 0
    for row in data:
        inputData, output = row.split(' | ')

        numToWord = getWordDictFromInput(inputData)

        total = ""
        # Count up total
        for word in output.split(' '):
            num = -1

            for i in numToWord:
                if numToWord[i] == set(word):
                    num = i
                    break
            total += str(num)
        ret += int(total)

    return ret


print(part1())
print(part2())
