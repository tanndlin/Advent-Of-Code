# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')


def getScoreOfLine(line):
    stack = [line[0]]
    lookup = {'}': '{', ']': '[', ')': '(', '>': '<'}
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    for char in line[1:]:
        if char in lookup:
            if stack[-1] == lookup[char]:
                stack.pop()
            else:
                return -1
        else:
            stack.append(char)

    score = 0
    for i in stack[::-1]:
        score *= 5
        score += scores[i]
    return score


def part1():
    ret = 0
    for line in data:
        stack = [line[0]]
        lookup = {'}': '{', ']': '[', ')': '(', '>': '<'}
        scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

        for char in line[1:]:
            if char in lookup:
                if stack[-1] == lookup[char]:
                    stack.pop()
                else:
                    # Get score of the first incorrect character
                    ret += scores[char]
                    break
            else:
                stack.append(char)

    return ret


def part2():
    scores = []
    for line in data:
        score = getScoreOfLine(line)
        if score != -1:
            scores.append(score)

    scores.sort()
    mid = len(scores) // 2
    return scores[mid]


print(part1())
print(part2())
