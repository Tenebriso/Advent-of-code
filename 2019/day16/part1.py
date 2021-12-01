pattern = [0, 1, 0, -1]


def read_input(input):
    with open(input) as fh:
        return [int(x) for x in fh.readline().strip()]


def compute_element(step, sequence):
    step_pattern = [y for t in [[x] * step for x in pattern] for y in t]
    shifted_pattern = step_pattern[1:]
    shifted_pattern.append(step_pattern[0])
    new_elem = 0
    i = step - 1
    while i < len(sequence):
        to_add = shifted_pattern[i % len(step_pattern)] * sequence[i]
        new_elem += to_add
        if i == 0 and step != 1:
            i += step - 1
        else:
            i += step
    return abs(new_elem) % 10


def compute_all_elements(sequence):
    all_elems = []
    for step in range(1, len(sequence)+1):
        all_elems.append(compute_element(step, sequence))
    return all_elems


def compute_phases(phases, sequence):
    for phase in range(1, phases + 1):
        sequence = compute_all_elements(sequence)
    return sequence



if __name__ == '__main__':
    input = "input"
    seq = read_input(input)
    # 24176176
    print(compute_phases(1, seq)[:8])
