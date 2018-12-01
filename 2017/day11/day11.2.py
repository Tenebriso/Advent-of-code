directions = {'s' : (0, +1, -1), 'n': (0, -1, +1),
        'sw': (-1, +1, 0), 'se': (+1, 0, -1),
        'nw': (-1, 0, +1), 'ne': (+1, -1, 0)}

def reader(filename):
    with open(filename) as f:
        for direction in f.read().strip().split(','):
            yield direction

def find_process(filename):
    direction_generator = reader(filename)
    current_dir= next(direction_generator)
    current_pos = (0, 0, 0)
    max_distance = 0
    while True:
        try:
            distance = directions[current_dir]
            current_pos = (current_pos[0] + distance[0],
                    current_pos[1] + distance[1],
                    current_pos[2] + distance[2])
            current_distance = (abs(current_pos[0]) + abs(current_pos[1]) +
                    abs(current_pos[2])) / 2
            if max_distance < current_distance:
                max_distance = current_distance
            current_dir= next(direction_generator)
        except StopIteration:
             break
    return max_distance 
            

if __name__ == '__main__':
    print find_process("input_file")

