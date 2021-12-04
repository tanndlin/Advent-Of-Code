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


def generateWinConditions(board, drawings):
    # Generate all possible win conditions

    # Generate all possible rows
    winConditions = []
    for row in board:
        winConditions.append(row)

    # Generate all possible columns
    for i in range(len(board)):
        col = []
        for j in range(len(board[i])):
            col.append(board[j][i])
        winConditions.append(col)

    return winConditions


def getEarliestWin(board):
    # Find the win condition that wins the earliest
    conditions = generateWinConditions(board, drawings)
    return min([max([drawings.index(i) for i in condition]) for condition in conditions])


def getResult(winner, drawIndex):
    # Forumla is sum of all non-called numbers * last called number
    total = 0
    for i in boards[winner]:
        for j in i:
            if j not in drawings[:drawIndex+1]:
                total += j

    return total * drawings[drawIndex]


def part1():
    m = len(drawings)
    winner = -1

    # Find the board that wins the earliest
    for i, board in enumerate(boards):
        earliestWin = getEarliestWin(board)
        if earliestWin < m:
            m = earliestWin
            winner = i

    return getResult(winner, m)


def part2():
    # Find the board that wins the latest
    winOrders = [getEarliestWin(board) for board in boards]
    m = max(winOrders)
    winner = winOrders.index(m)

    return getResult(winner, m)


print(part1())
print(part2())
