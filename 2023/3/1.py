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


def is_part_number(engine, i, j, length):
    res = False
    # current line
    if j > 0:
        res = res or is_symbol(engine, i, j -1)
    jj = j
    while jj < len(engine[i]) and engine[i][jj].isdigit():
        jj += 1
    if jj < len(engine[i]):
        res = res or is_symbol(engine, i, jj)
    # line above
    if i > 0:
        res = res or is_symbol_on_line(engine, i - 1, j, length)
    # line below
    if i < len(engine) - 1:
        res = res or is_symbol_on_line(engine, i + 1, j, length)
    return res


def is_symbol(engine, i, j):
    return not engine[i][j].isdigit() and not engine[i][j].isalpha() and engine[i][j] != '.'


def is_symbol_on_line(engine, i, j, length):
    start = j - 1
    end = j + length + 1
    res = False
    for ii in range(start, end):
        if ii >= 0 and ii < len(engine[i]):
            res = res or is_symbol(engine,i , ii)
    return res


def get_number(engine, i, j):
    number = int(engine[i][j])
    length = 1
    while j + length < len(engine[i]) and engine[i][j+length].isdigit():
        number = number * 10 + int(engine[i][j+length])
        length += 1
    return number


engine = read_engine()
print(engine)
total = 0
for i in range(len(engine)):
    j = 0
    while j < len(engine[i]):
        if engine[i][j].isdigit():
            number = get_number(engine, i, j)
            length = len(str(number))
            if is_part_number(engine, i, j, length):
                total += number
            j += length
        else:
            j += 1

print(total)
