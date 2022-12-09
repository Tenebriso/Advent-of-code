def is_touching(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


def move_knot(knot, direction):
    if direction == 'R':
        knot[1] += 1
    elif direction == 'L':
        knot[1] -= 1
    elif direction == 'U':
        knot[0] += 1
    elif direction == 'D':
        knot[0] -= 1
    else:
        raise Exception("Invalid direction")


def move_tail_to_head(head, tail):
    x_distance = head[0] - tail[0]
    y_distance = head[1] - tail[1]
    if x_distance < 0:
        move_knot(tail, 'D')
    elif x_distance > 0:
        move_knot(tail, 'U')
    if y_distance < 0:
        move_knot(tail, 'L')
    elif y_distance > 0:
        move_knot(tail, 'R')


def move_rope(rope_length):
    rope = [[0, 0] for _ in range(rope_length)]
    seen_points = set([(0, 0)])
    with open("input") as fp:
        for line in fp:
            direction, distance = line.strip().split()
            for i in range(int(distance)):
                # move head
                move_knot(rope[0], direction)
                # move rest of body if needed
                for knot_idx in range(0, rope_length - 1):
                    if is_touching(rope[knot_idx], rope[knot_idx + 1]):
                        break
                    move_tail_to_head(rope[knot_idx], rope[knot_idx + 1])
                    seen_points.add(tuple(rope[rope_length - 1]))
    return len(seen_points)


print(f"Part one = {move_rope(2)}")
print(f"Part two = {move_rope(10)}")
