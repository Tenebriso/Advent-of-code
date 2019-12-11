"""
You've just said goodbye to the rebooted rover and left Mars when you receive a faint distress
signal coming from the asteroid belt. It must be the Ceres monitoring station!

In order to lock on to the signal, you'll need to boost your sensors. The Elves send up the latest
BOOST program - Basic Operation Of System Test.

While BOOST (your puzzle input) is capable of boosting your sensors, for tenuous safety reasons,
it refuses to do so until the computer it runs on passes some checks to demonstrate it is a complete
Intcode computer.

Your existing Intcode computer is missing one key feature: it needs support for parameters in
relative mode.

Parameters in mode 2, relative mode, behave very similarly to parameters in position mode:
    the parameter is interpreted as a position.
    Like position mode, parameters in relative mode can be read from or written to.

The important difference is that relative mode parameters don't count from address 0.
Instead, they count from a value called the relative base. The relative base starts at 0.

The address a relative mode parameter refers to is itself plus the current relative base.
When the relative base is 0, relative mode parameters and position mode parameters with the same
value refer to the same address.

For example, given a relative base of 50, a relative mode parameter of -7 refers to
memory address 50 + -7 = 43.

The relative base is modified with the relative base offset instruction:

Opcode 9 adjusts the relative base by the value of its only parameter.
The relative base increases (or decreases, if the value is negative) by the value of the parameter.
For example, if the relative base is 2000, then after the instruction 109,19,
the relative base would be 2019.
If the next instruction were 204,-34, then the value at address 1985 would be output.

Your Intcode computer will also need a few other capabilities:

The computer's available memory should be much larger than the initial program.
Memory beyond the initial program starts with the value 0 and can be read or written
like any other memory. (It is invalid to try to access memory at a negative address, though.)
The computer should have support for large numbers. Some instructions near the beginning of the
BOOST program will verify this capability.
Here are some example programs that use these features:

109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99 takes no input and produces
a copy of itself as output.
1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
104,1125899906842624,99 should output the large number in the middle.
The BOOST program will ask for a single input; run it in test mode by providing it the value 1.
It will perform a series of checks on each opcode, output any opcodes (and the associated
parameter modes) that seem to be functioning incorrectly, and finally output a BOOST keycode.

Once your Intcode computer is fully functional, the BOOST program should report no malfunctioning
opcodes when run in test mode; it should only output a single value, the BOOST keycode.
What BOOST keycode does it produce?

Your puzzle answer was 3839402290.

--- Part Two ---
You now have a complete Intcode computer.

Finally, you can lock on to the Ceres distress signal! You just need to boost your sensors using
the BOOST program.

The program runs in sensor boost mode by providing the input instruction the value 2.
Once run, it will boost the sensors automatically, but it might take a few seconds to complete the
operation on slower hardware. In sensor boost mode, the program will output a single value:
    the coordinates of the distress signal.

Run the BOOST program in sensor boost mode. What are the coordinates of the distress signal?
"""

# SYSTEM_ID = 1
SYSTEM_ID = 2

def get_input(input_file):
    """ Read input file and transpose to a list of integers """
    with open(input_file) as intcode_file:
        int_codes = intcode_file.readline().split(',')
        int_codes = [int(int_code) for int_code in int_codes]
    return int_codes


def get_param(int_codes, mode, pos, offset, relative_base):
    """ Given the int codes, the mode of the parameter (positional, immediate, relative),
    its distance from the current pos (offset), relative  base value,
    compute the value of the parameter and return it """
    if mode == 0:
        try:
            param_pos = int_codes[pos + offset]
        except IndexError:
            int_codes.extend([0 for _ in range(pos + offset + 1)])
            param_pos = int_codes[pos + offset]
    elif mode == 1:
        param_pos = pos+ offset
    else:
        try:
            param_pos = int_codes[pos + offset] + relative_base
        except IndexError:
            int_codes.extend([0 for _ in range(pos + offset + 1)])
            param_pos = int_codes[pos + offset] + relative_base
    try:
        param = int_codes[param_pos]
    except IndexError:
        int_codes.extend([0 for _ in range(param_pos + 1)])

        param = int_codes[param_pos]
    return param


def parse_int_code(int_codes, code, pos, relative_base=0):
    """ Get the code and extract from it the opt_code and the input_mode for the params
    and then get the params depending on the input_code:
        input_code = 0, get the value at the position indicated by the first parameter
        input_code = 1, get the value of the first parameter """
    opt_code = code % 100
    mode_1 = (code // 100) % 10
    mode_2 = (code // 1000) % 10
    mode_3 = (code // 10000) % 10
    param_1 = get_param(int_codes, mode_1, pos, 1, relative_base)
    if opt_code in [1, 2, 7, 8, 5, 6]:
        param_2 = get_param(int_codes, mode_2, pos, 2, relative_base)
    else:
        param_2 = None
    if opt_code in [1, 2, 7, 8]:
        if mode_3 == 2:
            param_3 = int_codes[pos + 3] + relative_base
        else:
            param_3 = int_codes[pos + 3]
        if len(int_codes) < param_3:
            int_codes.extend([0 for _ in range(param_3 + 1)])
    else:
        param_3 = None

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
    relative_base = 0
    while pos < len(int_codes):
        code = int_codes[pos]
        opt_code, param_1, param_2, param_3 = parse_int_code(int_codes, code, pos, relative_base)
        if opt_code == 3:
            # takes an integer as input and saves it to the position given by its only parameter
            if (code // 100) % 10 == 2:
                pos_1 = int_codes[pos + 1] + relative_base
            else:
                pos_1 = int_codes[pos + 1]
            if len(int_codes) < pos_1:
                int_codes.extend([0 for _ in range(pos_1 + 1)])
            int_codes[pos_1] = SYSTEM_ID
            pos += 2
            continue
        if opt_code == 4:
            # outputs the value at the position provided by its only parameter
            print(param_1)
            pos += 2
            continue
        if opt_code == 99:
            break
        if opt_code == 9:
            # change the relative base to the new value
            relative_base += param_1
            pos += 2
            continue
        code_to_operation = {1: add, 2: multiply, 7: less_than, 8: equal}
        try:
            output = code_to_operation[opt_code](param_1, param_2)
            int_codes[param_3] = output
            pos += 4
            continue
        except KeyError:
            if (opt_code == 5 and param_1 != 0) or \
                (opt_code == 6 and param_1 == 0):
                pos = param_2
                continue
            else:
                pos += 3
                continue
        # No known code
        pos += 1


if __name__ == '__main__':
    INT_CODES = get_input('small_input')
    parse_int_codes(INT_CODES)
