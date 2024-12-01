def parse_line(line):
    line = line.strip().split("=")
    line[1] = line[1].replace('(', '').replace(')', '').strip().split(',')
    return {line[0].strip(): {'L': line[1][0].strip(), 'R': line[1][1].strip()}}


def count_steps_to_destination(source, destination, directions, points):
    steps = 0
    idx = 0
    while source != destination:
        # loop
        if idx == len(directions):
            idx = 0
        source = points[source][directions[idx]]
        idx += 1
        steps += 1
    return steps


with open("input") as input_file:
    directions = input_file.readline().strip()
    input_file.readline()
    points = parse_line(input_file.readline().strip())
    first_point = list(points.keys())[0]
    for line in input_file:
        points = {**parse_line(line), **points}
    print(count_steps_to_destination('AAA', 'ZZZ', directions, points))

