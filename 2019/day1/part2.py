import math


def get_module_fuel_fuel(fuel):
    if fuel <= 0:
        return 0
    fuel_fuel = math.floor(fuel/3) - 2
    if fuel_fuel <= 0:
        return 0

    return fuel_fuel + get_module_fuel_fuel(fuel_fuel)

if __name__ == '__main__':
    total_fuel = 0
    with open('large_input', 'r') as input_file:
        for line in input_file:
            module_mass = int(line.strip())
            total_fuel += get_module_fuel_fuel(module_mass)

    print(total_fuel)

