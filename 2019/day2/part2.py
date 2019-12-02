"""
To complete the gravity assist, you need to determine what pair of inputs produces
the output 19690720.

The inputs should still be provided to the program by replacing the values at addresses 1 and 2,
just like before. In this program, the value placed in address 1 is called the noun,
and the value placed in address 2 is called the verb.
Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also just like before.
Each time you try a pair of inputs, make sure you first reset the computer's memory to the values
in the program (your puzzle input) - in other words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output 19690720.
What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)

Your puzzle answer was 5485.
"""

import copy

def get_input(input_file):
    """ Read input file and transpose to a list of integers """
    with open(input_file) as intcode_file:
        int_codes = intcode_file.readline().split(',')
        int_codes = [int(int_code) for int_code in int_codes]
    return int_codes


def parse_int_codes(int_codes):
    """ Go over the list of intcodes and modify them accordingly """
    pos = 0
    while pos < len(int_codes):
        code = int_codes[pos]
        pos_1 = int_codes[pos + 1]
        pos_2 = int_codes[pos + 2]
        pos_3 = int_codes[pos + 3]
        if code == 1:
            sum_int_codes = int_codes[pos_1] + int_codes[pos_2]
            int_codes[pos_3] = sum_int_codes
        elif code == 2:
            multiply_int_codes = int_codes[pos_1] * int_codes[pos_2]
            int_codes[pos_3] = multiply_int_codes
        elif code == 99:
            break
        else:
            print("Unknown code %d", code)
            break
        pos += 4
    return int_codes[0]


def find_noun_and_verb(initial_int_codes, desired_output):
    """ Go over the list of intcodes and modify them accordingly until we reach the correct
    noun and verb and return them """
    for noun in range(100):
        for verb in range(100):
            int_codes = copy.deepcopy(initial_int_codes)
            int_codes[1] = noun
            int_codes[2] = verb
            if parse_int_codes(int_codes) == desired_output:
                return noun, verb
    print("Couldn't find them")
    return None, None


if __name__ == '__main__':
    INT_CODES = get_input('small_input')
    NOUN, VERB = find_noun_and_verb(INT_CODES, 19690720)
    print(100 * NOUN + VERB)
