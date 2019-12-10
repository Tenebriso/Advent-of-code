"""
It's no good - in this configuration, the amplifiers can't generate a large enough output signal to
produce the thrust you'll need. The Elves quickly talk you through rewiring the amplifiers into a
feedback loop:
      O-------O  O-------O  O-------O  O-------O  O-------O
0 -+->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-.
   |  O-------O  O-------O  O-------O  O-------O  O-------O |
   |                                                        |
   '--------------------------------------------------------+
                                                            |
                                                            v
                                                     (to thrusters)
Most of the amplifiers are connected as they were before;
amplifier A's output is connected to amplifier B's input, and so on.
However, the output from amplifier E is now connected into amplifier A's input.
This creates the feedback loop: the signal will be sent through the amplifiers many times.

In feedback loop mode, the amplifiers need totally different phase settings: integers from 5 to 9,
again each used exactly once. These settings will cause the Amplifier Controller Software to
repeatedly take input and produce output many times before halting.
Provide each amplifier its phase setting at its first input instruction;
all further input/output instructions are for signals.

Don't restart the Amplifier Controller Software on any amplifier during this process.
Each one should continue receiving and sending signals until it halts.

All signals sent or received in this process will be between pairs of amplifiers except the very
first signal and the very last signal.
To start the process, a 0 signal is sent to amplifier A's input exactly once.

Eventually, the software on the amplifiers will halt after they have processed the final loop.
When this happens, the last output signal from amplifier E is sent to the thrusters.
Your job is to find the largest output signal that can be sent to the thrusters using the new phase
settings and feedback loop arrangement.

Here are some example programs:

Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):

3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):

3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
Try every combination of the new phase settings on the amplifier feedback loop.
What is the highest signal that can be sent to the thrusters?
"""
import queue
import concurrent.futures
import itertools

INPUTS = []

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


def parse_int_codes(input_file_name, amp_nb):
    """ Go over the list of intcodes and modify them accordingly
    input_mode should be 0 or 1:
        0 = positional mode
        1 = input mode """
    pos = 0
    int_codes = get_input(input_file_name)
    while pos < len(int_codes):
        code = int_codes[pos]
        if code == 3:
            # takes an integer as input and saves it to the position given by its only parameter
            pos_1 = int_codes[pos + 1]
            int_codes[pos_1] = INPUTS[amp_nb].get()
            pos += 2
            continue
        elif code == 4:
            # outputs the value at the position provided by its only parameter
            pos_1 = int_codes[pos + 1]
            result = int_codes[pos_1]
            if amp_nb == 4:
                # last amplifier feeds the first
                INPUTS[0].put(result)
            else:
                # each amplifier feeds the next one
                INPUTS[amp_nb + 1].put(result)
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
            if (opt_code == 5 and param_1 != 0) or (opt_code == 6 and param_1 == 0):
                pos = param_2
                continue
            else:
                pos += 3
                continue
            pos += 1
    return result


def compute_max_output(input_file_name):
    """ Go over each possible permutation of phase settings and pass them to each amplifier,
    get the outputs and return the largest one """
    max_output = 0
    for perm in itertools.permutations(range(5, 10)):
        # each amplifier has its queue where it gets its input from
        global INPUTS
        INPUTS = [queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue()]
        # each amplifier is given its phase_setting
        for amp_nb, phase_setting in enumerate(perm):
            INPUTS[amp_nb].put(phase_setting)
        # first amplifier get signal 0 as first signal
        INPUTS[0].put(0)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # each amplifier runs in its own thread
            futures = [executor.submit(parse_int_codes, input_file_name, amp_nb)
                       for amp_nb, phase_setting in enumerate(perm)]
            # get the max from all the results
            current_output = max([future.result() for future in futures])
            # is it the biggest max we're encountered?
            if current_output > max_output:
                max_output = current_output
    return max_output


if __name__ == '__main__':
    print(compute_max_output('small_input'))
