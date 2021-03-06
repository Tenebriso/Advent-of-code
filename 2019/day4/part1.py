"""
You arrive at the Venus fuel depot only to discover it's protected by a password.
The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease;
they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?
"""

PUZZLE_INPUT = "183564-657474"



def check_number(number):
    """ Check that the given number meets the requirements,
    return True if it does, False otherwise """
    if ''.join(sorted(str(number))) != str(number):
        return False
    if len(set(str(number))) == len(str(number)):
        return False
    return True


def get_password_count():
    """ Count the number of numbers that meet the criteria in the given range """
    first_number, second_number = PUZZLE_INPUT.split('-')
    count = 0
    for number in range(int(first_number), int(second_number) + 1):
        if check_number(number):
            count += 1
    return count

print(get_password_count())
