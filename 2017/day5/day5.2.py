def escape(labyrinth):
    current = 0
    steps = 0
    while (current >= 0 and current < len(labyrinth)):
        jump = current + labyrinth[current]
        steps += 1
        if labyrinth[current] < 3:
            labyrinth[current] += 1
        else:
            labyrinth[current] -= 1
        current = jump
    return steps


if __name__ == '__main__':
    with open('input_file') as f:
        labyrinth = map(int, f.read().split())
    print(escape(labyrinth))
