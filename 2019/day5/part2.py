"""
Fortunately, the diagnostic program (your puzzle input) is already equipped for this.
Unfortunately, your Intcode computer is not.

Your computer is only missing a few opcodes:

Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to
                          the value from the second parameter. Otherwise, it does nothing.
Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to
                           the value from the second parameter. Otherwise, it does nothing.
Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the
                       position given by the third parameter. Otherwise, it stores 0.
Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the
                    position given by the third parameter. Otherwise, it stores 0.
Like all instructions, these instructions need to support parameter modes as described above.

Normally, after an instruction is finished, the instruction pointer increases by the number of
values in that instruction. However, if the instruction modifies the instruction pointer, that value
is used and the instruction pointer is not automatically increased.

For example, here are several programs that take one input, compare it to the value 8,
and then produce one output:

3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8;
                           output 1 (if it is) or 0 (if it is not).
3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8;
                           output 1 (if it is) or 0 (if it is not).
3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8;
                         output 1 (if it is) or 0 (if it is not).
3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8;
                        output 1 (if it is) or 0 (if it is not).
Here are some jump tests that take an input, then output 0 if the input was zero or 1
if the input was non-zero:

3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
Here's a larger example:

3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
The above example program uses an input instruction to ask for a single number.
The program will then output 999 if the input value is below 8, output 1000 if the input value is
equal to 8, or output 1001 if the input value is greater than 8.

This time, when the TEST diagnostic program runs its input instruction to get the ID of the system
to test, provide it 5, the ID for the ship's thermal radiator controller.
This diagnostic test suite only outputs one number, the diagnostic code.

What is the diagnostic code for system ID 5?

Your puzzle answer was 236453.
"""

SYSTEM_ID = 5

def get_input(input_file):
    """ Read input file and transpose to a list of integers """
    with open(input_file) as intcode_file:
        int_codes = intcode_file.readline().split(',')
        int_codes = [int(int_code) for int_code in int_codes]
    return int_codes


def parse_int_code(int_codes, code, pos):
    """ Get the code and extract from it the opt_code and the input_mode for the params
    and then get the params depending on the input_code:
        input_code = 0, get the value at the position indicated by the first parameter
        input_code = 1, get the value of the first parameter """
    opt_code = code % 100
    mode_1 = (code // 100) % 10
    mode_2 = (code // 1000) % 10
    if mode_1 == 0:
        param_1 = int_codes[int_codes[pos+1]]
    else:
        param_1 = int_codes[pos+1]
    if mode_2 == 0:
        param_2 = int_codes[int_codes[pos+2]]
    else:
        param_2 = int_codes[pos+2]
    param_3 = int_codes[pos+3]
    return opt_code, param_1, param_2, param_3


def add(val_1, val_2):
    """ Add val_1 and val_2 """
    return val_1 + val_2


def multiply(val_1, val_2):
    """ Multiply val_1 and val_2 """
    return val_1 * val_2


def less_than(val_1, val_2):
    """ Return 1 if val_1 < val_2, 0 otherwise """
    return int(val_1 < val_2)


def equal(val_1, val_2):
    """ Return 1 if val_1 == val_2, 0 otherwise """
    return int(val_1 == val_2)


def parse_int_codes(int_codes):
    """ Go over the list of intcodes and modify them accordingly
    input_mode should be 0 or 1:
        0 = positional mode
        1 = input mode """
    pos = 0
    while pos < len(int_codes):
        code = int_codes[pos]
        if code == 3:
            # takes an integer as input and saves it to the position given by its only parameter
            pos_1 = int_codes[pos + 1]
            int_codes[pos_1] = SYSTEM_ID
            pos += 2
            continue
        elif code == 4:
            # outputs the value at the position provided by its only parameter
            pos_1 = int_codes[pos + 1]
            print(int_codes[pos_1])
            pos += 2
            continue
        elif code == 99:
            break
        opt_code, param_1, param_2, param_3 = parse_int_code(int_codes, code, pos)
        code_to_operation = {1: add, 2: multiply, 7: less_than, 8: equal}
        try:
            output = code_to_operation[opt_code](param_1, param_2)
            int_codes[param_3] = output
            pos += 4
        except KeyError:
            if (opt_code == 5 and param_1 != 0) or \
                (opt_code == 6 and param_1 == 0):
                pos = param_2
                continue
            else:
                pos += 3
                continue
            pos += 1


if __name__ == '__main__':
    INT_CODES = get_input('small_input')
    parse_int_codes(INT_CODES)
