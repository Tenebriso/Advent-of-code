from collections import namedtuple

Coordinates = namedtuple('Coordinates', ['up_left_x', 'up_left_y', 'low_right_x', 'low_right_y'])


def read_input(filename):
    all_squares = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.split()
            upper_left = line[2][0:-1].split(',')
            upper_left = (int(upper_left[0]), int(upper_left[1]))
            low_right = line[3].split('x')
            low_right = (int(low_right[0]) + upper_left[0], int(low_right[1]) + upper_left[1])
            all_squares.append(Coordinates(up_left_x = upper_left[0], up_left_y=upper_left[1],
                    low_right_x=low_right[0], low_right_y=low_right[1]))

    return all_squares


def determine_overlapping(filename):
    coord_gen = read_input(filename)
    existing_coords = set()
    overlapping_coords = set()
    total_inches = 0
    for coordinates in coord_gen:
        for x in range(coordinates.up_left_x, coordinates.low_right_x):
                for y in range(coordinates.up_left_y, coordinates.low_right_y):
                    if (x, y) in existing_coords:
                        overlapping_coords.add((x, y))
                    else:
                        existing_coords.add((x, y))
    return len(overlapping_coords)

if __name__ == '__main__':
    print determine_overlapping("input")






