from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def read_maze_and_start_pos():
    maze = []
    start = []
    with open("input") as input_file:
        i = 0
        for line in input_file:
            line = line.strip()
            maze.append(list(line))
            start_pos = line.find('S')
            if start_pos != -1:
                start = [i, start_pos]
            i += 1
    return maze, start


def find_next_steps(maze, start):
    i, j = start
    steps = []
    if i > 0:
        if maze[i-1][j] in 'F7|':
            steps.append([i-1, j])
    if j > 0:
        if maze[i][j-1] in '-FL':
            steps.append([i, j-1])
    if i < len(maze) - 1:
        if maze[i+1][j] in 'JL|':
            steps.append([i+1, j])
    if j < len(maze[i]) - 1:
        if maze[i][j+1] in '-FL':
            steps.append([i, j+1])
    return steps


def find_next_step(maze, current_pipe, previous_pipe):
    i, j = 0, 1
    if maze[current_pipe[i]][current_pipe[j]] == '-':
        if current_pipe[i] != previous_pipe[i]:
            return None
        # go right
        if previous_pipe[j] < current_pipe[j]:
            if current_pipe[j] == len(maze[current_pipe[i]]) - 1:
                return None
            return [current_pipe[i], current_pipe[j] + 1]
        # go left
        if current_pipe[j] == 0:
            return None
        return [current_pipe[i], current_pipe[j] - 1]
    if maze[current_pipe[i]][current_pipe[j]] == '|':
        if current_pipe[j] != previous_pipe[j]:
            return None
        # go down
        if previous_pipe[i] < current_pipe[i]:
            if current_pipe[i] == len(maze) - 1:
                return None
            return [current_pipe[i] + 1, current_pipe[j]]
        # go up
        if current_pipe[i] == 0:
            return None
        return [current_pipe[i] - 1, current_pipe[j]]
    if maze[current_pipe[i]][current_pipe[j]] == 'F':
        if previous_pipe[i] < current_pipe[i] or previous_pipe[j] < current_pipe[j]:
            return None
        # from below, go right
        if previous_pipe[i] > current_pipe[i]:
            if current_pipe[j] == len(maze[i]) - 1:
                return None
            return [current_pipe[i], current_pipe[j] + 1]
        # from right, go below
        # if previous_pipe[j] > current_pipe[j]:
        if current_pipe[i] == len(maze) - 1:
            return None
        return [current_pipe[i]+ 1, current_pipe[j]]
    if maze[current_pipe[i]][current_pipe[j]] == 'L':
        if previous_pipe[i] > current_pipe[i] or previous_pipe[j] < current_pipe[j]:
            return None
        # go right
        if previous_pipe[i] < current_pipe[i]:
            if current_pipe[j] == len(maze[i]) - 1:
                return None
            return [current_pipe[i], current_pipe[j] + 1]
        # go up
        if current_pipe[i] == 0:
            return None
        return [current_pipe[i] - 1, current_pipe[j]]
    if maze[current_pipe[i]][current_pipe[j]] == 'J':
        if previous_pipe[i] > current_pipe[i] or previous_pipe[j] > current_pipe[j]:
            return None
        # go left
        if previous_pipe[i] < current_pipe[i]:
            if current_pipe[j] == 0:
                return None
            return [current_pipe[i], current_pipe[j] - 1]
        # go up
        if current_pipe[i] == 0:
            return None
        return [current_pipe[i] -1, current_pipe[j]]
    if maze[current_pipe[i]][current_pipe[j]] == '7':
        if previous_pipe[j] > current_pipe[j] or previous_pipe[i] < current_pipe[i]:
            return None
        # go left, from below
        if previous_pipe[i] > current_pipe[i]:
            if current_pipe[j] == 0:
                return None
            return [current_pipe[i], current_pipe[j] - 1]
        # go down, from left
        if current_pipe[i] == len(maze) - 1:
            return None
        return [current_pipe[i] + 1, current_pipe[j]]
    if maze[current_pipe[i]][current_pipe[j]] == 'S':
        return current_pipe
    return None


maze, start = read_maze_and_start_pos()
possible_next_steps = find_next_steps(maze, start)
for step in possible_next_steps:
    # print(maze[start[0]][start[1]])
    total = 1
    current = step
    previous = start
    next = find_next_step(maze, current, previous)
    loop = [start]
    while current != next and next is not None:
        # print(maze[current[0]][current[1]])
        loop.append(current)
        previous = current
        current = next
        next = find_next_step(maze, current, previous)
        total += 1
    if next is None:
        print(f"{step} leads nowhere!!")
    else:
        print(f"{total} steps in the loop")
        break  # found the loop

total_points = 0
polygon = Polygon(loop)
for i in range(len(maze)):
    for j in range(len(maze[i])):
        point = Point(i, j)
        if polygon.contains(point):
            total_points += 1
print(total // 2)
print(total_points)
