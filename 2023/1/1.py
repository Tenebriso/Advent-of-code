def get_first_digit(input_string):
    for character in input_string:
        if character.isdigit():
            return character

def get_last_digit(input_string):
    for character in input_string[::-1]:
        if character.isdigit():
            return character

total = 0
with open('input') as input_file:
    for line in input_file:
        first_digit = get_first_digit(line)
        last_digit = get_last_digit(line)
        total += (int(first_digit) * 10 +
                  int(last_digit))

print(total)
