def read_grid():
    grid = []
    with open("input") as fp:
        for i, line in enumerate(fp):
            grid.append([])
            for j, tree in enumerate(line.strip()):
                grid[i].append(int(tree))
    return grid


def left_check(grid):
    left = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if j == 0 or left[i][j - 1][0] < col:
                left[i][j] = (col, j)
            else:
                left[i][j] = left[i][j - 1]
    return left


def right_check(grid):
    right = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i, row in enumerate(grid):
        for j in range(len(row) - 1, -1, -1):
            if j == len(row) - 1 or right[i][j + 1][0] < grid[i][j]:
                right[i][j] = (grid[i][j], j)
            else:
                right[i][j] = right[i][j + 1]
    return right


def up_check(grid):
    up = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if i == 0 or up[i - 1][j][0] < grid[i][j]:
                up[i][j] = (grid[i][j], i)
            else:
                up[i][j] = up[i - 1][j]
    return up


def down_check(grid):
    down = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for j in range(len(grid[0])):
        for i in range(len(grid) - 1, -1, -1):
            if i == len(grid) - 1 or down[i+1][j][0] < grid[i][j]:
                down[i][j] = (grid[i][j], i)
            else:
                down[i][j] = down[i + 1][j]
    return down


def is_tree_visible(grid, i, j, checks):
    # margin is always visible
    if i == 0 or j == 0 or i == (len(grid) - 1) or j == (len(grid[0]) - 1):
        return True
    if checks["left"][i][j][1] >= j or checks["right"][i][j][1] <= j or \
            checks["up"][i][j][1] >= i or checks["down"][i][j][1] <= i:
        return True
    return False


def total_visible_trees(grid, checks):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_tree_visible(grid, i, j, checks):
                total += 1
    return total


def right_score(grid, i, j, checks):
    if j == len(grid[0]) - 1 or j == len(grid[0]) - 2 or checks['right'][i][j][1] == j:
        return len(grid[0]) - j - 1
    score = checks['right'][i][j][1] - j
    for ii in range(1, score + 1):
        if grid[i][j + ii] >= grid[i][j]:
            return ii
    return score


def left_score(grid, i, j, checks):
    if j == 0 or j == 1 or checks['left'][i][j][1] == j:
        return j
    score = j - checks['left'][i][j][1]
    for ii in range(1, score + 1):
        if grid[i][j - ii] >= grid[i][j]:
            return ii
    return score


def down_score(grid, i, j, checks):
    if i == len(grid) - 1 or i == len(grid) - 2 or checks['down'][i][j][1] == i:
        return len(grid) - 1 - i
    score = checks['down'][i][j][1] - i
    for ii in range(1, score + 1):
        if grid[i + ii][j] >= grid[i][j]:
            return ii
    return score


def up_score(grid, i, j, checks):
    if i == 1 or i == 0 or checks['up'][i][j][1] == i:
        return i
    score = i - checks['up'][i][j][1]
    for ii in range(1, score + 1):
        if grid[i - ii][j] >= grid[i][j]:
            return ii
    return score


def tree_scenic_score(grid, i, j, checks):
    return left_score(grid, i, j, checks) * right_score(grid, i, j, checks) * \
           up_score(grid, i, j, checks) * down_score(grid, i, j, checks)


def max_scenic_score(grid, checks):
    return max(
        [tree_scenic_score(grid, i, j, checks) for i in range(1, len(grid) - 1)
         for j in range(1, len(grid[0]) - 1)])


def solve(part):
    grid = read_grid()
    checks = {"left": left_check(grid),
              "right": right_check(grid),
              "up": up_check(grid),
              "down": down_check(grid)}
    if part == 1:
        return total_visible_trees(grid, checks)
    elif part == 2:
        return max_scenic_score(grid, checks)


print(f"Part one = {solve(1)}")
print(f"Part two = {solve(2)}")
