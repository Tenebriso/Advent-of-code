def parse_instruction(instruction):
    value_to_add = 0
    if instruction[0] == 'noop':
        cycles = 1
    else:
        cycles = 2
        value_to_add = int(instruction[1])
    return cycles, value_to_add


def run_cycles(cycles, cycle, x):
    for _ in range(cycles):
        draw_crt(cycle, x)
        cycle += 1
    return cycle


def draw_crt(cycle, x):
    if cycle % 40 == 0 and cycle != 0:
        print()
    if abs(x - (cycle % 40)) <= 1:
        print('#', end='')
    else:
        print('.', end='')


def solve(signal_cycle=20, max_signal_cycle=220, signal_step=40):
    cycle = 0
    x = 1
    signal_strength = 0
    with open("input") as fp:
        for line in fp:
            line = line.strip().split()
            cycles, value_to_add = parse_instruction(line)
            cycle = run_cycles(cycles, cycle, x)
            if signal_cycle <= max_signal_cycle and cycle >= signal_cycle:
                signal_strength += (signal_cycle * x)
                signal_cycle += signal_step
            # end of cycle
            x += value_to_add
    print()
    return signal_strength


print(f"Part one = {solve()}")