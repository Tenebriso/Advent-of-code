"""
The Thermal Environment Supervision Terminal (TEST) starts by running a diagnostic program
(your puzzle input).
The TEST diagnostic program will run on your existing Intcode computer after a few modifications:

First, you'll need to add two new instructions:

Opcode 3 takes a single integer as input and saves it to the position given by its only parameter.
    For example, the instruction 3,50 would take an input value and store it at address 50.
Opcode 4 outputs the value of its only parameter.
    For example, the instruction 4,50 would output the value at address 50.
Programs that use these instructions will come with documentation that explains what should be
connected to the input and output.
The program 3,0,4,0,99 outputs whatever it gets as input, then halts.

Second, you'll need to add support for parameter modes:
Each parameter of an instruction is handled based on its parameter mode.
Right now, your ship computer already understands parameter mode 0, position mode,
which causes the parameter to be interpreted as a position - if the parameter is 50,
its value is the value stored at address 50 in memory.
Until now, all parameters have been in position mode.

Now, your ship computer will also need to handle parameters in mode 1, immediate mode.
In immediate mode, a parameter is interpreted as a value - if the parameter is 50, its value is 50.

Parameter modes are stored in the same value as the instruction's opcode.
The opcode is a two-digit number based only on the ones and tens digit of the value, that is,
the opcode is the rightmost two digits of the first value in an instruction.
Parameter modes are single digits, one per parameter, read right-to-left from the opcode:
    the first parameter's mode is in the hundreds digit,
    the second parameter's mode is in the thousands digit,
    the third parameter's mode is in the ten-thousands digit, and so on.
Any missing modes are 0.

For example, consider the program 1002,4,3,4,33.

The first instruction, 1002,4,3,4, is a multiply instruction - the rightmost two digits of the first
value, 02, indicate opcode 2, multiplication. Then, going right to left, the parameter modes are 0
(hundreds digit), 1 (thousands digit), and 0 (ten-thousands digit, not present and therefore zero):

ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
This instruction multiplies its first two parameters.
The first parameter, 4 in position mode, works like it did before - its value is the value
stored at address 4 (33). The second parameter, 3 in immediate mode, simply has value 3.
The result of this operation, 33 * 3 = 99, is written according to the third parameter,
4 in position mode, which also works like it did before - 99 is written to address 4.

Parameters that an instruction writes to will never be in immediate mode.

Finally, some notes:

It is important to remember that the instruction pointer should increase by the number of values in
the instruction after the instruction finishes. Because of the new instructions,
this amount is no longer always 4.
Integers can be negative: 1101,100,-1,4,0 is a valid program
(find 100 + -1, store the result in position 4).
The TEST diagnostic program will start by requesting from the user the ID of the system to test
by running an input instruction - provide it 1, the ID for the ship's air conditioner unit.

It will then perform a series of diagnostic tests confirming that various parts of the
Intcode computer, like parameter modes, function correctly.
For each test, it will run an output instruction indicating how far the result of the test was from
the expected value, where 0 means the test was successful.
Non-zero outputs mean that a function is not working correctly; check the instructions that were run
before the output instruction to see which one failed.

Finally, the program will output a diagnostic code and immediately halt.
This final output isn't an error; an output followed immediately by a halt means
the program finished.
If all outputs were zero except the diagnostic code, the diagnostic program ran successfully.

After providing 1 to the only input instruction and passing all the tests,
what diagnostic code does the program produce?

Your puzzle answer was 13547311.
"""

SYSTEM_ID = 1

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
    if opt_code != 1 and opt_code != 2:
        return opt_code, None, None, None
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
        code_to_operation = {1: add, 2: multiply}
        try:
            output = code_to_operation[opt_code](param_1, param_2)
            int_codes[param_3] = output
            pos += 4
        except KeyError:
            pos += 1


if __name__ == '__main__':
    INT_CODES = get_input('small_input')
    parse_int_codes(INT_CODES)
