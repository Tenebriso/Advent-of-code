DIGITS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
          'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5',
          '6', '7', '8', '9']

def get_first_and_last_digit(input_string):
    first_digit, min_index = None, len(input_string)
    last_digit, max_index = None, 0
    for digit_index, digit in enumerate(DIGITS):
        first = get_first_digit_and_index(line, digit, digit_index, min_index)
        if first != None:
            min_index, first_digit = first
        last = get_last_digit_and_index(line, digit, digit_index,
                                        max_index)
        if last != None:
            max_index, last_digit = last

    return first_digit * 10 + last_digit


def get_first_digit_and_index(input_string, digit, digit_index, min_index):
    first_index = input_string.find(digit)
    if first_index == -1:
       return None
    if min_index < first_index:
       return None
    min_index = first_index
    try:
        return (first_index, int(digit))
    except ValueError:
        return (first_index, digit_index)


def get_last_digit_and_index(input_string, digit, digit_index, max_index):
    last_index = input_string.rfind(digit)
    if max_index > last_index:
        return None
    max_index = last_index
    try:
        return (max_index, int(digit))
    except ValueError:
        return (max_index, digit_index)


total = 0
with open('input') as input_file:
    for line in input_file:
        total += get_first_and_last_digit(line.lower())

print(total)


