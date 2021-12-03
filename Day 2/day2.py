data = open("input.txt", 'r').read().split('\n')


data = [x.split(' ') for x in data]


x = 0
y = 0
aim = 0

for i in data:
    if i[0] == "forward":
        x += int(i[1])
        y += int(i[1]) * aim
    if i[0] == "up":
        aim -= int(i[1])
    if i[0] == "down":
        aim += int(i[1])

print(x, y)
print(x * y)
