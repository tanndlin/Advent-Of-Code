# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')


def convertToBag(bag):
    if "no other bags" in bag:
        return (0, bag)
    bag = bag.split(' ')
    amount = int(bag[0])
    name = ' '.join(bag[1:-1]) + " bags"
    return (amount, name)


bags = {}

for bag in data:
    bagName = bag.split(' contain ')[0]
    bagContains = bag.split(' contain ')[1].split(', ')
    if bagContains == ['no other bags']:
        bag[bagName] = []
    else:
        contents = [convertToBag(bag) for bag in bagContains]
        bags[bagName] = contents


def canContainGold(bagName, bags):
    if 'shiny gold' in bagName:
        return True

    return any(canContainGold(bag, bags) for num, bag in bags[bagName] if "no other" not in bag)


def part1():
    total = 0
    for bag in bags:
        if "shiny gold" in bag:
            continue
        if canContainGold(bag, bags):
            total += 1

    return total


def part2():
    def countBags(bagName, bags):
        if "no other" in bagName:
            return 0

        total = 0
        for num, bag in bags[bagName]:
            # print(num, bag)
            total += num * (countBags(bag, bags)+1)

        return total

    return countBags('shiny gold bags', bags)


print(part1())
print(part2())
