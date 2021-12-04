# data = open('simple.txt', 'r').read().split('\n\n')
data = open('input.txt', 'r').read().split('\n\n')

data = [i.split('\n') for i in data]


def part1():
    total = 0
    for group in data:
        questions = set()
        for person in group:
            for q in person:
                questions.add(q)

        total += len(questions)

    return total


def part2():
    total = 0
    for group in data:
        yes = set(group[0])
        for person in group[1:]:
            yes = yes.intersection(set(person))

        total += len(yes)

    return total


print(part1())
print(part2())
