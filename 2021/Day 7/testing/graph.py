import matplotlib.pyplot as plt

data = open('data.txt', 'r').read().split(',')
data = [int(x) for x in data]


def linear_cost(a, b):
    return abs(a - b)


def increasing_cost(a, b):
    n = abs(a - b)
    return n * (n+1) // 2


values_linear = []
values_increasing = []
for i in range(max(data)):
    cost_linear = 0
    cost_increasing = 0
    for j in data:
        cost_linear += linear_cost(i, j)
        cost_increasing += increasing_cost(i, j)
    values_linear.append(cost_linear)
    values_increasing.append(cost_increasing)


xs = [x for x in range(max(data))]
ys = values_linear

fig, axs = plt.subplots(2)
# Plot data
axs[0].plot(xs, ys)

# Plot the increasing data
axs[1].plot(xs, values_increasing)

plt.show()


# There are no local minima judging by the graph
# meaning starting at the average and using gradient descent is a good approach
