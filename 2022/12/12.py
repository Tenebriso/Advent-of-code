from collections import deque


def read_input():
    start = None
    end = None
    starts = []
    heightmap = []
    with open("input") as fp:
        for line in fp:
            heightmap.append([x for x in line.strip()])
            if 'S' in line:
                start = (len(heightmap) - 1, line.index('S'))
                heightmap[start[0]][start[1]] = 'a'
            if 'E' in line:
                end = (len(heightmap) - 1, line.index('E'))
                heightmap[end[0]][end[1]] = 'z'
            for i, height in enumerate(heightmap[len(heightmap) - 1]):
                if height == 'a':
                    starts.append((len(heightmap) - 1, i))
    return start, end, heightmap, starts


def check_neighbors(i, j, heightmap, queue, distances, seen):
    if i != 0:
        if ord(heightmap[i - 1][j]) - ord(heightmap[i][j]) <= 1 and (i - 1, j) not in seen:
            distances[(i - 1, j)] = distances[(i, j)] + 1
            queue.append((i - 1, j))
            seen.add((i - 1, j))
    if i != len(heightmap) - 1:
        if ord(heightmap[i + 1][j]) - ord(heightmap[i][j]) <= 1 and (i + 1, j) not in seen:
            queue.append((i + 1, j))
            distances[(i + 1, j)] = distances[(i, j)] + 1
            seen.add((i + 1, j))
    if j != 0:
        if ord(heightmap[i][j - 1]) - ord(heightmap[i][j]) <= 1 and (i, j - 1) not in seen:
            queue.append((i, j - 1))
            seen.add((i, j - 1))
            distances[(i, j - 1)] = distances[(i, j)] + 1
    if j != len(heightmap[0]) - 1:
        if ord(heightmap[i][j + 1]) - ord(heightmap[i][j]) <= 1 and (i, j + 1) not in seen:
            queue.append((i, j + 1))
            seen.add((i, j + 1))
            distances[(i, j + 1)] = distances[(i, j)] + 1


def shortest_path(start, end, heightmap):
    seen = set([start])
    distances = {start: 0}
    queue = deque([start])
    while queue:
        i, j = queue.popleft()
        if (i, j) == end:
            return distances[(i, j)]
        check_neighbors(i, j, heightmap, queue, distances, seen)


def shortest_path_all_starts(starts, end, heightmap):
    min_dist = 10000
    for start in starts:
        dist = shortest_path(start, end, heightmap)
        if dist and dist < min_dist:
            min_dist = dist
    return min_dist


def solve(part):
    start, end, heightmap, starts = read_input()
    if part == 1:
        return shortest_path(start, end, heightmap)
    elif part == 2:
        return shortest_path_all_starts(starts, end, heightmap)


print(f"Part one = {solve(1)}")
print(f"Part two = {solve(2)}")
