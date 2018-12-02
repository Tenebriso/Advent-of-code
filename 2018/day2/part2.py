'''
This module solves the first challenge of day #2 of Advent of Code 2018.
Takes as input a file of IDs and returns the checksum
'''

INPUT_FILE = 'input'

def ids_reader(filename):
    ''' Function that goes over each ID in the file
    and appends it to a list of IDs that is then returned'''
    ids = []
    with open(filename) as input_file:
        for line in input_file:
            ids.append(line.strip())
    return ids


def detect_correct(id1, id2):
    ''' Check if two ids have only one letter difference.
    The first return value, ``diff`` is True if they are correct
    and False otherwise.
    The second return value, ``letter`` is the index of the letter
    where they differ'''
    diff = False
    letter = None
    for idx, letter1 in enumerate(id1):
        if letter1 != id2[idx]:
            if diff:
                return False, None
            else:
                letter = idx
                diff = True
    return diff, letter


def find_correct(filename):
    ''' Given a list of IDs, find the pair of IDs that
    only differ in one letter and return the resulting ID if
    that letter is removed'''
    ids = ids_reader(filename)
    for i in range(len(ids) - 1):
        for j in range(i + 1, len(ids)):
            correct, letter = detect_correct(ids[i], ids[j])
            if correct:
                return ids[i][:letter] + ids[i][letter+1:]
    return ''


if __name__ == '__main__':
    print find_correct(INPUT_FILE)
