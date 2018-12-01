'''
This module solves the first challenge of day #1 of Advent of Code 2018.
Takes as input a file of frequency changes and returns the final frequency
'''

INPUT_FILE = "input"

def frequency_parser(filename):
    ''' Generator function that go over each element in the file,
    converts it to int and returns it '''
    with open(filename) as input_file:
        for line in input_file:
            yield int(line.strip())

def compute_frequency(filename):
    ''' Function that goes over all the frequency changes and computes
    the resulting frequency. Add each frequency change to the old frequency
    until you reach the end '''
    parser = frequency_parser(filename)
    frequency = 0
    while True:
        try:
            frequency += next(parser)
        except StopIteration:
            break
    return frequency

if __name__ == '__main__':
    print compute_frequency(INPUT_FILE)
