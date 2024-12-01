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


def get_differences_until_zero_from_end(history):
    difference_matrix = deque()
    differences = get_differences(history)
    while len(set(differences)) != 1 or 0 not in set(differences):
        difference_matrix.appendleft(differences)
        differences = get_differences(differences)
    return ([history[-1]] + [x[-1] for x in difference_matrix], [x[0] for x in difference_matrix] + [history[0]])


def get_prediction_at_start(differences):
    prediction = 0
    for difference in differences:
        prediction = difference - prediction
    return prediction


total_end_prediciton = 0
total_start_prediction = 0
for history in read_histories():
    end, beginning = get_differences_until_zero_from_end(history)
    # part 1
    total_end_prediciton += sum(end)
    # part 2
    total_start_prediction += get_prediction_at_start(beginning)
print(f"part 1 = {total_end_prediciton}")
print(f"part 2 = {total_start_prediction}")
