import math


def get_module_fuel(mass):
    return math.floor(mass / 3) - 2


if __name__ == '__main__':
    total_fuel = 0
    with open('small_input', 'r') as input_file:
        for line in input_file:
            module_mass = int(line.strip())
            total_fuel += get_module_fuel(module_mass)

    print(total_fuel)

