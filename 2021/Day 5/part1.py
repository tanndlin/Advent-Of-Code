data = open('simple.txt', 'r').read().split('\n')
# data = open('input.txt', 'r').read().split('\n')


def genPoints(x1, x2):
    points = []

    if x1 < x2:
        for i in range(x1, x2+1):
            points.append(i)
    else:
        for i in range(x1, x2-1, -1):
            points.append(i)

    return points


used = {}

for line in data:
    p1 = line.split(' -> ')[0]
    p2 = line.split(' -> ')[1]

    x1, y1 = p1.split(',')
    x2, y2 = p2.split(',')

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    if x1 == x2:
        for i in genPoints(y1, y2):
            if (x1, i) in used:
                used[(x1, i)] += 1
            else:
                used[(x1, i)] = 1
    elif y1 == y2:
        for i in genPoints(x1, x2):
            if (i, y1) in used:
                used[(i, y1)] += 1
            else:
                used[(i, y1)] = 1


overlaps = 0
for point in used:
    if used[point] > 1:
        overlaps += 1

print(overlaps)
