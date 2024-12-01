def read_engine():
    engine = []
    with open('input') as input_file:
        i = 0
        for line in input_file:
            engine.append([])
            for character in line.strip():
                    engine[i].append(character)
            i += 1
    return engine


def get_engine_power(engine, i, j):
    power = 1
    total_part_numbers = 0
    # current line
    if j > 0:
        number = get_number_to_left(engine, i, j-1)
        if number:
            total_part_numbers += 1
            power *= int(number)
    if j < len(engine[i]) - 1:
        number = get_number_to_right(engine, i, j+1)
        if number:
            total_part_numbers += 1
            power *= int(number)
    # line above
    if i > 0:
        number, touched_part_numbers = get_power_on_line(engine, i-1, j)
        if number:
            total_part_numbers += touched_part_numbers
            power *= int(number)
    # line below
    if i < len(engine) - 1:
        number, touched_part_numbers = get_power_on_line(engine, i+1, j)
        if number:
            total_part_numbers += touched_part_numbers
            power *= int(number)
    if total_part_numbers >= 2:
        return power
    return 0


def is_gear(engine, i, j):
    return engine[i][j] == '*'


def get_number_to_left(engine, i, j):
    if not engine[i][j].isdigit():
        return ""
    number = engine[i][j]
    length = 1
    while j - length >= 0 and engine[i][j-length].isdigit():
        number = engine[i][j-length] + number
        length += 1
    return number

def get_number_to_right(engine, i, j):
    if not engine[i][j].isdigit():
        return ""
    number = engine[i][j]
    length = 1
    while j + length < len(engine[i]) and engine[i][j+length].isdigit():
        number = number + engine[i][j+length]
        length += 1
    return number

def get_power_on_line(engine, i, j):
    number = ""
    part_numbers_count = 0
    if j > 0:
        number = get_number_to_left(engine, i, j-1) + number
        if number:
            part_numbers_count += 1
    if engine[i][j].isdigit():
        number += engine[i][j]
        if j < len(engine[i]) - 1:
            number += get_number_to_right(engine, i, j+1)
        if number:
            return int(number), 1 # one number per line
    if j < len(engine[i]) - 1:
        right = get_number_to_right(engine, i, j+1)
        if right:
            part_numbers_count += 1
        if number and right:
            return int(number) * int(right), part_numbers_count
        if number:
            return int(number), part_numbers_count
        if right:
            return int(right), part_numbers_count
        return 0, part_numbers_count
    if number:
        return int(number), part_numbers_count
    return 0, part_numbers_count


engine = read_engine()
total = 0
for i in range(len(engine)):
    for j in range(len(engine[i])):
        if is_gear(engine, i, j):
            number = get_engine_power(engine, i, j)
            total += number

print(total)
