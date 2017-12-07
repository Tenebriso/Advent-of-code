from collections import namedtuple
import pprint
import copy
import re

Program = namedtuple('Program', ['name', 'weight', 'held_programs'])

def find_bottom(programs):
    ''' Return the bottom program of the towe '''
    # programs that hold other programs
    holders = [key for key in programs
                if programs[key].held_programs is not None]
    backup = copy.copy(holders)
    for holder in holders:
        held_programs = programs[holder].held_programs
        for held in held_programs:
            if held in backup:
                backup.remove(held)
    return programs[backup[0]]


def is_balanced(programs, current):
    '''
    Check if a program in balanced:
    all the programs it holds have the same weight
    '''
    if current.held_programs is None:
        return True
    else:
        return len(set([find_weight(programs, programs[x])
                        for x in current.held_programs])) == 1


def find_weight(programs, current):
    '''
    Find the total weight of a program:
    add its weight with the weights of all the programs it holds
    '''
    if current.held_programs is None:
        return current.weight
    weight = 0
    for held in current.held_programs:
        weight += find_weight(programs, programs[held])
    return weight + current.weight


def unbalanced_helper(programs, current):
    ''' Return the program which has children of different weights '''
    while not is_balanced(programs, current):
        new = None
        for held in current.held_programs:
            if not is_balanced(programs, programs[held]):
                new = programs[held]
                break
        if new is None:
            return current
        else:
            current = new

def find_unbalanced(programs):
    ''' Return the weight the program should have to balance the tower '''
    unbalanced = unbalanced_helper(programs, find_bottom(programs))
    # find out of place child of unbalanced program
    ww = [find_weight(programs, programs[x])
            for x in unbalanced.held_programs]
    out_of_place = [x for x in unbalanced.held_programs
                    if ww.count(find_weight(programs, programs[x])) == 1][0]
    # the offset
    difference = set([find_weight(programs, programs[x])
                        for x in unbalanced.held_programs])
    d = abs(list(difference)[1] - list(difference)[0])
    # determine if bigger or smaller
    weight = find_weight(programs, programs[out_of_place])
    v = difference.pop()
    if v == weight:
        v = difference.pop()
    if weight < v:
        return programs[out_of_place].weight + d
    else:
        return programs[out_of_place].weight - d


if __name__ == '__main__':
    programs = {}
    # read input
    with open('input_file') as f:
        while True:
            line = f.readline().split()
            if len(line) == 2:
                programs[line[0]] = Program(
                    name=line[0],
                    weight=int(filter(str.isdigit, line[1])),
                    held_programs=None
                )
            elif len(line) < 2:
                break
            else:
                held = []
                for program in line[3:]:
                    held.append(program.strip(','))
                programs[line[0]] = Program(
                    name=line[0],
                    weight=int(filter(str.isdigit, line[1])),
                    held_programs=held
                )
    # print final result
    print(find_unbalanced(programs))
