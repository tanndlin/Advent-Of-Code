# data = open('simple.txt', 'r').read().split('\n\n')
data = open('input.txt', 'r').read().split('\n\n')

drawings = [int(i) for i in data[0].split(',')]

boards = []
for i in data[1:]:
    board = i.split('\n')
    for j in range(len(board)):
        row = []
        for k in board[j].split(' '):
            if k != '':
                row.append(int(k))
        board[j] = row
    boards.append(board)


def checkWin(board, nums):
    # Check for bingo
    for row in board:
        if all([i in nums for i in row]):
            return True

    for i in range(len(board)):
        col = []
        for j in range(len(board[i])):
            col.append(board[j][i])

        if all([j in nums for j in col]):
            return True
    return False


def getResult(board, nums):
    total = 0
    for i in board:
        for j in i:
            if j not in nums:
                total += j

    return total * nums[-1]


def part1():
    winner = False
    drawIndex = 1

    while not winner and drawIndex < len(drawings):
        winner = any([checkWin(board, drawings[:drawIndex+1])
                      for board in boards])

        if not winner:
            drawIndex += 1

    for i, board in enumerate(boards):
        if checkWin(board, drawings[:drawIndex+1]):
            return getResult(board, drawings[:drawIndex+1])


def part2():
    haveWon = [False for i in boards]
    drawIndex = 1

    while haveWon.count(False) > 1:
        for i, board in enumerate(boards):
            if not haveWon[i]:
                if checkWin(board, drawings[:drawIndex+1]):
                    haveWon[i] = True
        drawIndex += 1

    return getResult(boards[haveWon.index(False)], drawings[:drawIndex+1])


print(part1())
print(part2())
