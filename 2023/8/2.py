from math import gcd


def lcm(numbers):
    lcm = 1
    for number in numbers:
        lcm = lcm * number // gcd(lcm, number)
    return lcm


def parse_line(line):
    line = line.strip().split("=")
    line[1] = line[1].replace('(', '').replace(')', '').strip().split(',')
    return {line[0].strip(): {'L': line[1][0].strip(), 'R': line[1][1].strip()}}


def count_steps_to_destination(source, directions, points):
    steps = 0
    idx = 0
    while not source.endswith('Z'):
        # loop
        if idx == len(directions):
            idx = 0
        source = points[source][directions[idx]]
        idx += 1
        steps += 1
    return steps


points = {}
with open("input") as input_file:
    directions = input_file.readline().strip()
    input_file.readline()
    sources = {}
    for line in input_file:
        current_points = parse_line(line)
        source = list(current_points.keys())[0]
        if source.endswith('A'):
            sources[source] = False
        points = {**current_points, **points}

steps = []
for source in sources:
    steps.append(count_steps_to_destination(source, directions, points))
print(lcm(steps))
