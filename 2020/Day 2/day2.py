# data = open('simple.txt', 'r').read().split('\n')
data = open('input.txt', 'r').read().split('\n')


def part1():
    valid = 0

    for line in data:
        split = line.split(' ')
        times = split[0]

        low = times.split('-')[0]
        high = times.split('-')[1]
        letter = split[1][0]
        password = split[2]

        count = password.count(letter)
        if count >= int(low) and count <= int(high):
            valid += 1
    print(valid)


def part2():
    valid = 0

    for line in data:
        split = line.split(' ')
        times = split[0]

        left = times.split('-')[0]
        right = times.split('-')[1]
        letter = split[1][0]
        password = split[2]

        left = password[int(left) - 1] == letter
        right = password[int(right) - 1] == letter

        valid += not (left and right) and (left or right)

    print(valid)


part1()
part2()
