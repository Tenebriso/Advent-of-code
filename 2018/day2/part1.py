'''This module solves the first challenge of day #2 of Advent of Code 2018.
Takes as input a file of IDs and returns the checksum'''

INPUT_FILE = 'input'

def id_generator(filename):
    ''' Generator function that goes over each ID in the file and returns it'''
    with open(filename) as input_file:
        for line in input_file:
            yield line.strip()


def count_occ(box_id):
    ''' Function that counts the occurences of letters in an ID.
    The first return value in the touple is 1 if there are letters that
    appear two times. The second element of the touple is 1 if there are
    letters that appear three times.'''
    occ = {}
    for letter in box_id:
        try:
            occ[letter] += 1
        except KeyError:
            occ[letter] = 1
    if occ.values().count(2) and occ.values().count(3):
        return (1, 1)
    elif occ.values().count(2):
        return(1, 0)
    elif occ.values().count(3):
        return (0, 1)
    return (0, 0)


def calculate_checksum(filename):
    ''' Calculate checksum of IDs by multiplying the number of IDs that
    contain letter that appear 2 times with the number of IDs that contain
    letters that appear 3 times'''
    gen = id_generator(filename)
    two, three = 0, 0
    while True:
        try:
            box_id = next(gen)
            counts = count_occ(box_id)
            two += counts[0]
            three += counts[1]
        except StopIteration:
            break
    return two * three


if __name__ == '__main__':
    print calculate_checksum(INPUT_FILE)
