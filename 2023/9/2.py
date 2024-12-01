from collections import deque


def read_histories():
    histories = []
    with open("input") as input_file:
        for line in input_file:
            history = [int(x) for x in line.strip().split()]
            histories.append(history)
    return histories


def get_differences(history):
    differences = []
    for i, val in enumerate(history[:len(history)-1]):
        differences.append(history[i + 1] - val)
    return differences


def get_differences_until_zero(history):
    difference_matrix = deque()
    differences = get_differences(history)
    while len(set(differences)) != 1 or 0 not in set(differences):
        difference_matrix.appendleft(differences)
        differences = get_differences(differences)
    return [history[-1]] + [x[-1] for x in difference_matrix]


total = 0
for history in read_histories():
    total += sum(get_differences_until_zero(history))
print(total)