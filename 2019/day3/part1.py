"""
Opening the front panel reveals a jumble of wires.
Specifically, two wires are connected to a central port and extend outward on a grid.
You trace the path each wire takes as it leaves the central port,
one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths.
To fix the circuit, you need to find the intersection point closest to the central port.
Because the wires are on a grid, use the Manhattan distance for this measurement.
While the wires do technically cross right at the central port where they both start,
this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o),
it goes right 8, up 5, left 5, and finally down 3:
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port:
    its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?

Your puzzle answer was 2427.
"""

from collections import namedtuple

Position = namedtuple('Position', 'x y')

def get_wires_path(input_file):
    """ Read the file containing the movements of the two wires """
    with open(input_file) as wires_path_file:
        first_wire_path = wires_path_file.readline().split(',')
        second_wire_path = wires_path_file.readline().split(',')
    return first_wire_path, second_wire_path


def compute_distance(current_position):
    """ Compute the distance from 0,0 to the current position """
    distance = abs(current_position.x) + abs(current_position.y)
    return distance


def move_on_grid(current_pos, axis, number_of_moves, direction, seen_positions):
    """ Move from the current position to the position at number_of_moves away,
    moving on the x or y axis or up/down left/righ, recording each touched position """
    if direction == -1:
        number_of_moves *= (-1)
    if axis == 'x':
        for current_x in range(current_pos.x, current_pos.x + number_of_moves, direction):
            new_current_pos = Position(x=current_x, y=current_pos.y)
            seen_positions.add(new_current_pos)
    else:
        for current_y in range(current_pos.y, current_pos.y + number_of_moves, direction):
            new_current_pos = Position(x=current_pos.x, y=current_y)
            seen_positions.add(new_current_pos)

    return new_current_pos, seen_positions


def walk_wire(wire_path):
    """ Go over the movements specified and record each position touched
    in a set of seen_positions  """
    current_pos = Position(0, 0)
    seen_positions = set()
    for move in wire_path:
        number_of_movements = int(move[1::]) + 1
        if move.startswith('D'):
            current_pos, seen_positions = move_on_grid(
                current_pos, 'y', number_of_movements, -1, seen_positions)
        elif move.startswith('U'):
            current_pos, seen_positions = move_on_grid(
                current_pos, 'y', number_of_movements, +1, seen_positions)
        elif move.startswith('L'):
            current_pos, seen_positions = move_on_grid(
                current_pos, 'x', number_of_movements, -1, seen_positions)
        elif move.startswith('R'):
            current_pos, seen_positions = move_on_grid(
                current_pos, 'x', number_of_movements, +1, seen_positions)

    return seen_positions


def get_min_distance(wire_1_positions, wire_2_positions):
    """ Find the minimum distance between the intersections of the two wires and position 0, 0 """
    intersections = wire_1_positions & wire_2_positions
    closest_distance = 100000
    for position in intersections:
        current_distance = compute_distance(position)
        if current_distance < closest_distance and current_distance > 0:
            closest_distance = current_distance

    return closest_distance


if __name__ == '__main__':
    PATH_1, PATH_2 = get_wires_path('small_input')
    FIRST_POSITIONS = walk_wire(PATH_1)
    SECOND_POSITIONS = walk_wire(PATH_2)
    print(get_min_distance(FIRST_POSITIONS, SECOND_POSITIONS))
