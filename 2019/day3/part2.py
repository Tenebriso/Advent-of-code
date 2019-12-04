"""
It turns out that this circuit is very timing-sensitive;
you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection;
choose the intersection where the sum of both wires' steps is lowest.
If a wire visits a position on the grid multiple times, use the steps value from the first time
it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to
that location, including the intersection being considered. Again consider the example from above:

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
In the above example, the intersection closest to the central port is reached after
8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for
a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15
and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?
"""

from collections import namedtuple
import part1

Position = namedtuple('Position', 'x y')

def move_on_grid(current_pos, axis, number_of_moves, direction, seen_positions,
                 distances, current_distance):
    """ Move from the current position to the position at number_of_moves away,
    moving on the x or y axis or up/down left/righ, recording each touched position """
    if direction == -1:
        number_of_moves *= (-1)
    if axis == 'x':
        for current_x in range(current_pos.x, current_pos.x + number_of_moves, direction):
            new_current_pos = Position(x=current_x, y=current_pos.y)
            seen_positions.add(new_current_pos)
            if not new_current_pos in distances:
                distances[new_current_pos] = current_distance
                current_distance += 1
    else:
        for current_y in range(current_pos.y, current_pos.y + number_of_moves, direction):
            new_current_pos = Position(x=current_pos.x, y=current_y)
            seen_positions.add(new_current_pos)
            if not new_current_pos in distances:
                distances[new_current_pos] = current_distance
                current_distance += 1

    return new_current_pos, seen_positions, distances, current_distance


def walk_wire(wire_path):
    """ Go over the movements specified and record each position touched
    in a set of seen_positions  """
    current_pos = Position(0, 0)
    seen_positions = set()
    distances = {}
    current_distance = 0
    for move in wire_path:
        number_of_movements = int(move[1::]) + 1
        if move.startswith('D'):
            current_pos, seen_positions, distances, current_distance = move_on_grid(
                current_pos, 'y', number_of_movements, -1, seen_positions,
                distances, current_distance)
        elif move.startswith('U'):
            current_pos, seen_positions, distances, current_distance = move_on_grid(
                current_pos, 'y', number_of_movements, +1,
                seen_positions, distances, current_distance)
        elif move.startswith('L'):
            current_pos, seen_positions, distances, current_distance = move_on_grid(
                current_pos, 'x', number_of_movements, -1,
                seen_positions, distances, current_distance)
        elif move.startswith('R'):
            current_pos, seen_positions, distances, current_distance = move_on_grid(
                current_pos, 'x', number_of_movements, +1,
                seen_positions, distances, current_distance)

    return seen_positions, distances


def get_min_steps(first_positions, first_distances, second_positions, second_distances):
    """ Compute the minimum number of steps from both wires to an intersection """
    min_steps = 100000
    intersections = first_positions & second_positions
    for intersection in intersections:
        if intersection.x == 0 and intersection.y == 0:
            continue
        steps = first_distances[intersection] + second_distances[intersection]
        if steps < min_steps:
            min_steps = steps
    return min_steps


if __name__ == '__main__':
    PATH_1, PATH_2 = part1.get_wires_path('small_input')
    FIRST_POSITIONS, FIRST_DISTANCES = walk_wire(PATH_1)
    SECOND_POSITIONS, SECOND_DISTANCES = walk_wire(PATH_2)
    print(get_min_steps(FIRST_POSITIONS, FIRST_DISTANCES, SECOND_POSITIONS, SECOND_DISTANCES))
