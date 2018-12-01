def reader(filename):
    with open(filename) as f:
        for line in f:
            yield line


def check_condition(first_val, condition, second_val):
    return eval("{} {} {}".format(first_val, condition, second_val))


def resulted_value(instruction, value):
    if instruction == 'dec':
        return -value
    return value


if __name__ == '__main__':
    r = reader('input_file')
    registers = {}
    while True:
        try:
            words = r.next().strip().split()
        except StopIteration:
            break
        if words[0] not in registers:
            registers[words[0]] = 0
        if words[4] not in registers:
            registers[words[4]] = 0
        if check_condition(registers[words[4]], words[5], int(words[6])):
            registers[words[0]] += resulted_value(words[1], int(words[2]))
    print(max(registers.values()))
