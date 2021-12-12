# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')

connections = {}

for line in data:
    a, b = line.split('-')
    if a in connections:
        connections[a].append(b)
    else:
        connections[a] = [b]

    if b in connections:
        connections[b].append(a)
    else:
        connections[b] = [a]


def countDoubles(path):
    s = set(path)
    total = 0
    for cave in s:
        if cave.islower() and path.count(cave) > 1:
            total += 1
    return total


def part1(start, path):
    if start == "end":
        path.append(start)
        return 1

    total = 0
    path.append(start)
    for cave in connections[start]:
        if cave in path and cave.islower():
            continue
        total += part1(cave, path.copy())

    return total

# TODO: dont use lists


def part2(start, path):
    path.append(start)
    if start == "end":
        return 1

    total = 0
    for cave in connections[start]:
        if cave in path and (cave == "start" or cave == "end"):
            continue
        if cave in path and cave.islower() and countDoubles(path) == 1:
            continue
        total += part2(cave, path.copy())

    return total


print(part1("start", []))
print(part2("start", []))
