# data = open('simple.txt', 'r').read()
data = open('input.txt', 'r').read()

dots, folds = data.split('\n\n')
dots = dots.split('\n')

dots = [dot.split(',') for dot in dots]
dots = [(int(x), int(y)) for x, y in dots]

folds = folds.split('\n')


for index, fold in enumerate(folds):
    fold = fold.split(' ')[-1]
    direction, line = fold.split('=')

    newDots = set()
    for dot in dots:
        x, y = dot
        if direction == 'y' and y > int(line):
            y = 2 * int(line) - y
        elif direction == 'x' and x > int(line):
            x = 2 * int(line) - x

        newDots.add((x, y))
        dots = list(newDots)

    if index == 0:
        print(f'Part 1: {len(dots)}')

    m = max([k[1] for k in dots]) + 1
    n = max([k[0] for k in dots]) + 1

for i in range(m):
    for j in range(n):
        if (j, i) in dots:
            print('#', end='')
        else:
            print('.', end='')
    print()
