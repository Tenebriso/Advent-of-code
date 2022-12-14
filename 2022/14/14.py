def parse_path(points, floor):
    prev, curr = None, None
    path = {}
    for point in points:
        point = [int(x) for x in point.split(',')]
        if point[1] > floor:
            floor = point[1]
        if not prev:
            prev = point
            continue
        curr = point
        # horizontal line
        if prev[0] == curr[0]:
            if prev[0] not in path:
                path[prev[0]] = set()
            for i in range(min(prev[1], curr[1]), max(prev[1], curr[1]) + 1):
                path[prev[0]].add(i)
        # vertical line
        elif prev[1] == curr[1]:
            for i in range(min(prev[0], curr[0]), max(curr[0], prev[0]) + 1):
                if i not in path:
                    path[i] = set()
                path[i].add(prev[1])
        prev = curr
    return path, floor


def build_paths():
    paths = {}
    floor = 0
    with open('input') as fp:
        for line in fp:
            line = line.strip().split(' -> ')
            path, floor = parse_path(line, floor)
            for row, cols in path.items():
                if row not in paths:
                    paths[row] = cols
                else:
                    paths[row] = paths[row].union(cols)
    return paths, floor


def rest_position(paths, sand_pos, floor=None):
    if sand_pos[0] not in paths:
        fall_on_floor(paths, sand_pos, floor)
        return False
    try:
        sand_pos[1] = min([x for x in paths[sand_pos[0]] if sand_pos[1] <= x])
    except ValueError:
        fall_on_floor(paths, sand_pos, floor)
        return False
    d = [sand_pos[0], sand_pos[1] - 1]  # down
    dl = [sand_pos[0] - 1, sand_pos[1]]  # down-left
    dr = [sand_pos[0] + 1, sand_pos[1]]  # down-right
    # down left
    if dl[0] not in paths or dl[1] not in paths[dl[0]]:
        return rest_position(paths, dl, floor)
    # down right
    if dr[0] not in paths or dr[1] not in paths[dr[0]]:
        return rest_position(paths, dr, floor)
    # nowhere to go
    paths[d[0]].add(d[1])
    return True


def fall_on_floor(paths, sand_pos, floor):
    if not floor:
        return
    if sand_pos[0] not in paths:
        paths[sand_pos[0]] = set()
    if floor in paths[sand_pos[0]]:
        paths[sand_pos[0]].add(sand_pos[1])
    else:
        paths[sand_pos[0]].add(floor - 1)


def part_one():
    paths, _ = build_paths()
    total = 0
    while rest_position(paths, [500, 0]):
        total += 1
    return total


def part_two():
    paths, floor = build_paths()
    floor += 2
    total = 0
    while 0 not in paths[500]:
        rest_position(paths, [500, 0], floor)
        total += 1
    return total


print(f"Part one = {part_one()}")
print(f"Part two = {part_two()}")
