"""
Based on the navigational maps, you're going to need to send more power to your ship's thrusters to
reach Santa in time. To do this, you'll need to configure a series of amplifiers already
installed on the ship.

There are five amplifiers connected in series; each one receives an input signal and produces an
output signal. They are connected such that the first amplifier's output leads to the second
amplifier's input, the second amplifier's output leads to the third amplifier's input, and so on.
The first amplifier's input value is 0, and the last amplifier's output leads to
your ship's thrusters.

    O-------O  O-------O  O-------O  O-------O  O-------O
0 ->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
    O-------O  O-------O  O-------O  O-------O  O-------O
The Elves have sent you some Amplifier Controller Software (your puzzle input),
a program that should run on your existing Intcode computer.
Each amplifier will need to run a copy of the program.

When a copy of the program starts running on an amplifier, it will first use an input instruction to
ask the amplifier for its current phase setting (an integer from 0 to 4).
Each phase setting is used exactly once, but the Elves can't remember which amplifier
needs which phase setting.

The program will then call another input instruction to get the amplifier's input signal,
compute the correct output signal, and supply it back to the amplifier with an output instruction.
(If the amplifier has not yet received an input signal, it waits until one arrives.)

Your job is to find the largest output signal that can be sent to the thrusters by trying every
possible combination of phase settings on the amplifiers. Make sure that memory is not shared or
reused between copies of the program.

For example, suppose you want to try the phase setting sequence 3,1,2,4,0, which would mean setting
amplifier A to phase setting 3, amplifier B to setting 1, C to 2, D to 4, and E to 0.
Then, you could determine the output signal that gets sent from amplifier E to the thrusters with
the following steps:

Start the copy of the amplifier controller software that will run on amplifier A.
At its first input instruction, provide it the amplifier's phase setting, 3.
At its second input instruction, provide it the input signal, 0.
After some calculations, it will use an output instruction to indicate the amplifier's output signal
Start the software for amplifier B. Provide it the phase setting (1) and then whatever output signal
was produced from amplifier A. It will then produce a new output signal destined for amplifier C.
Start the software for amplifier C, provide the phase setting (2) and the value from amplifier B,
then collect its output signal.
Run amplifier D's software, provide the phase setting (4) and input value,
and collect its output signal.
Run amplifier E's software, provide the phase setting (0) and input value,
and collect its output signal.
The final output signal from amplifier E would be sent to the thrusters.
However, this phase setting sequence may not have been the best one; another sequence might have
sent a higher signal to the thrusters.

Here are some example programs:

Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):

3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):

3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0
Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):

3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
Try every combination of phase settings on the amplifiers.
What is the highest signal that can be sent to the thrusters?
"""

import itertools

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


def parse_int_codes(int_codes, phase_setting, signal_strength):
    """ Go over the list of intcodes and modify them accordingly
    input_mode should be 0 or 1:
        0 = positional mode
        1 = input mode """
    pos, result = 0, 0
    while pos < len(int_codes):
        code = int_codes[pos]
        if code == 3:
            # takes an integer as input and saves it to the position given by its only parameter
            pos_1 = int_codes[pos + 1]
            int_codes[pos_1] = phase_setting
            phase_setting = signal_strength
            pos += 2
            continue
        elif code == 4:
            # outputs the value at the position provided by its only parameter
            pos_1 = int_codes[pos + 1]
            result = int_codes[pos_1]
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
    return result, int_codes


def compute_max_output_for_perm(perm, int_codes):
    """ For the given permutation, compute the maximum returned output """
    output, max_output = 0, 0
    for phase_setting in perm:
        output, int_codes = parse_int_codes(int_codes, phase_setting, output)
        if output > max_output:
            max_output = output
    return max_output


def compute_max_output(nb_amplifiers, input_file_name):
    """ Go over each possible permutation of phase settings and pass them to each amplifier,
    get the outputs and return the largest one """
    max_output = 0
    for perm in itertools.permutations(range(nb_amplifiers)):
        # reset int codes and signal strength
        int_codes = get_input(input_file_name)
        current_output = compute_max_output_for_perm(perm, int_codes)
        if current_output > max_output:
            max_output = current_output
    return max_output

if __name__ == '__main__':
    print(compute_max_output(5, 'small_input'))
