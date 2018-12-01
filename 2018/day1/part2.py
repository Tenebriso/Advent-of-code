'''
This module solves the second challenge of day #1 of Advent of Code 2018.
Takes as input a file of frequency changes and returns the first duplicate frequency
'''

from part1 import frequency_parser

INPUT_FILE = "input"


def detect_duplicate(filename):
    '''Iterate over each frequency change and check if it has already been seen before.
    Keep all frequencies in a ``Set``, return the first duplicate.
    Iterate multiple times over the list'''
    parser = frequency_parser(filename)
    frequency = 0
    frequencies = set([0])
    while True:
        try:
            frequency += next(parser)
            if frequency in frequencies:
                break
            else:
                frequencies.add(frequency)
        except StopIteration:
            parser = frequency_parser(filename)
    return frequency

if __name__ == '__main__':
    print detect_duplicate(INPUT_FILE)
