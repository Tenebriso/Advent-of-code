import re

INPUT_FILE = 'input'

def read_positions():
    initial_config = []
    with open(INPUT_FILE) as positions:
        for line in positions:
            initial_config.append(map(int, re.findall(r'-?\d+', line.strip())))
    return initial_config


def compute_min_box(initial_config):
    final_sec = 0 
    final_box = [10000, 0, 10000, 0]
    final_size = 200000
    for sec in range(1, 20000):
            minx = min(x + sec * vx for y, x, vy, vx in initial_config)
            miny = min(y + sec * vy for y, x, vy, vx in initial_config)
            maxx = max(x + sec * vx for y, x, vy, vx in initial_config)
            maxy = max(y + sec * vy for y, x, vy, vx in initial_config)
            current_size = abs(maxx - minx) + abs(maxy - miny)
            if current_size < final_size and current_size > 0:
                final_size = current_size
                final_sec = sec
                final_box = [minx, maxx, miny, maxy]
    return final_sec, final_box


def draw_letters(initial_configs, sec, box):
    final_results = set([(x + vx * sec, y + vy * sec) for y, x, vy, vx in initial_configs])
    for x in range(box[0], box[1] + 1):
        row = ''
        for y in range(box[2], box[3] + 1):
            if (x, y) in final_results:
                row += '#'
            else:
                row += '.'
        print row


if __name__ == '__main__':
    initial_configs = read_positions()
    sec, box = compute_min_box(initial_configs)
    print sec, box
    draw_letters(initial_configs, sec, box)
