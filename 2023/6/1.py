def read_inputs():
    with open("input") as input_file:
        times = input_file.readline().strip().split()[1::]
        distances = input_file.readline().strip().split()[1::]
    return [int(x) for x in times], [int(x) for x in distances]


times, distances = read_inputs()
total = 1
for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    possibilities = 0
    for acc in range(1, time // 2 + 1):
        if acc * (time - acc) > distance:
            if acc == time // 2 and time % 2 == 0:
                possibilities += 1
            else:
                possibilities += 2
    total *= possibilities
print(total)
