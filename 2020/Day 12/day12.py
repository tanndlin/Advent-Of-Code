# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part1():
    x = 0
    y = 0
    dirIndex = 1

    for i in data:
        op = i[0]
        val = int(i[1:])

        if op == 'N':
            y += val
        elif op == 'S':
            y -= val
        elif op == 'E':
            x += val
        elif op == 'W':
            x -= val
        elif op == 'L':
            dirIndex = (dirIndex - val // 90) % 4
        elif op == 'R':
            dirIndex = (dirIndex + val // 90) % 4
        elif op == 'F':
            x += dirs[dirIndex][0] * val
            y += dirs[dirIndex][1] * val

    return abs(x) + abs(y)


def part2():
    def rotate(ship, waypoint, times):

        if times > 0:
            for i in range(times):
                waypoint = (waypoint[1], -waypoint[0])
            return waypoint
        else:
            for i in range(abs(times)):
                waypoint = (-waypoint[1], waypoint[0])
            return waypoint

    shipX = 0
    shipY = 0
    waypointX = 10
    waypointY = 1

    for i in data:
        op = i[0]
        val = int(i[1:])
        if op == 'N':
            waypointY += val
        elif op == 'S':
            waypointY -= val
        elif op == 'E':
            waypointX += val
        elif op == 'W':
            waypointX -= val
        elif op == 'L':
            waypointX, waypointY = rotate(
                (shipY, shipY), (waypointX, waypointY), -val//90)
        elif op == 'R':
            waypointX, waypointY = rotate(
                (shipY, shipY), (waypointX, waypointY), val//90)
        elif op == 'F':
            shipX += waypointX * val
            shipY += waypointY * val
    return abs(shipX) + abs(shipY)


print(part1())
print(part2())
