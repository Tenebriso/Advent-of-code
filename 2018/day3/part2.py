from collections import namedtuple
from part1 import Coordinates


def read_input(filename):
    ''' Read file and generate a dictionary mapping the id to Coordinates.'''
    id_to_coordinates = {}
    with open(filename) as input_file:
        for line in input_file:
            line = line.split()
            upper_left = line[2][0:-1].split(',')
            upper_left = (int(upper_left[0]), int(upper_left[1]))
            low_right = line[3].split('x')
            low_right = (int(low_right[0]) + upper_left[0], int(low_right[1]) + upper_left[1])
            id_to_coordinates[line[0][1:]] = Coordinates(
                up_left_x=upper_left[0], up_left_y=upper_left[1], 
                low_right_x=low_right[0], low_right_y=low_right[1])
            return id_to_coordinates 


def determine_overlapping(filename):
    coord_gen = read_input(filename)
    existing_coords = set()
    overlapping_coords = set()
    for coordinates in coord_gen.values():
        for x in range(coordinates.up_left_x, coordinates.low_right_x):
            for y in range(coordinates.up_left_y, coordinates.low_right_y):
                if (x, y) in existing_coords:
                    overlapping_coords.add((x, y))
                else:
                    existing_coords.add((x, y))
    non_overlaps = existing_coords - overlapping_coords
    for claim_id, coordinates in coord_gen.iteritems():
        correct = True
        for x in range(coordinates.up_left_x, coordinates.low_right_x):
            for y in range(coordinates.up_left_y, coordinates.low_right_y):
                if (x, y) not in non_overlaps:
                    correct = False
                    break
                if not correct:
                    break
        if correct:
            return claim_id

    return None


if __name__ == '__main__':
    print determine_overlapping("input")
