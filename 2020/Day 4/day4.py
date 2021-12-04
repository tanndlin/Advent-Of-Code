# data = open('simple.txt', 'r').read().split('\n\n')
data = open('input.txt', 'r').read().split('\n\n')

data = [x.replace('\n', ' ') for x in data]
data = [x.split(' ') for x in data]

dicts = []
for passport in data:
    d = {}
    for field in passport:
        split = field.split(':')
        d[split[0]] = split[1]
    dicts.append(d)


def part1():
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    valid = 0
    for passport in dicts:
        flag = True
        for i in required:
            if i not in passport:
                flag = False

        valid += flag

    return valid


def part2():
    reqs = {"byr": lambda x: 1920 <= int(x) <= 2002,
            "iyr": lambda x: 2010 <= int(x) <= 2020,
            "eyr": lambda x: 2020 <= int(x) <= 2030,
            "hgt": lambda x: x[-2:] in ['cm', 'in'] and (int(x[:-2]) in range(150, 193+1) if x[-2:] == 'cm' else int(x[:-2]) in range(59, 76+1)),
            "hcl": lambda x: x[0] == '#' and len(x) == 7 and all(c in '0123456789abcdef' for c in x[1:]),
            "ecl": lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            "pid": lambda x: len(x) == 9 and all(c in '0123456789' for c in x)}

    valid = 0
    for passport in dicts:
        flag = True
        for i in reqs:
            if i not in passport:
                flag = False
            else:
                flag = flag and reqs[i](passport[i])

        valid += flag

    return valid


print(part1())
print(part2())
