from collections import namedtuple
import pprint
import copy
import re


def find_bottom(programs):
    holders = [key for key in programs if programs[key] is not None]
    backup = copy.copy(holders)
    for holder in holders:
        held_programs = programs[holder]
        for held in held_programs:
            if held in backup:
                backup.remove(held)
    return backup[0]


if __name__ == '__main__':
    programs = {}
    with open('input_file') as f:
        while True:
            line = f.readline().split()
            if len(line) == 2:
                programs[line[0]] = None
            elif len(line) < 2:
                break
            else:
                held = []
                for program in line[3:]:
                    held.append(program.strip(','))
                programs[line[0]] = held
    print(find_bottom(programs))
