# data = open('simple.txt', 'r').read().split('\n\n')
data = open('input.txt', 'r').read().split('\n\n')
drawings = [int(i) for i in data[0].split(',')]


def parseBoard(board):
    # Parse the board into a list of lists
    return [[int(i) for i in row.split(' ') if i != ''] for row in board.split('\n')]


boards = [parseBoard(board) for board in data[1:]]


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


def getResult(board, drawIndex):
    # Forumla is sum of all non-called numbers * last called number
    called = set(drawings[:drawIndex+1])
    total = 0

    for row in board:
        for i in row:
            if i not in called:
                total += i

    return total * drawings[drawIndex]


def part1():
    # Find the board that wins the earliest
    winOrders = [getEarliestWin(board) for board in boards]
    m = min(winOrders)
    winner = winOrders.index(m)

    return getResult(boards[winner], m)


def part2():
    # Find the board that wins the latest
    winOrders = [getEarliestWin(board) for board in boards]
    m = max(winOrders)
    winner = winOrders.index(m)

    return getResult(boards[winner], m)


print(part1())
print(part2())
