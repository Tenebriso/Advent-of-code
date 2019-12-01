import string


INPUT_FILE = 'input'

def letter_generator(filename):
    letters = []
    with open(filename) as input_file:
        char = input_file.read(1)
        while char:
            letters.append(char)
            char = input_file.read(1)
    return letters[:-1]


def find_remains(filename):
    letters = letter_generator(filename)
    min_polymer = len(letters)
    for letter in list(string.ascii_lowercase):
        intact = []
        for char in letters:
                if char.lower() == letter:
                    continue
                if not intact:
                    intact.append(char)
                    continue
                if intact[-1] != char and intact[-1].lower() == char.lower():
                       intact.pop()
                else:
                    intact.append(char)
        if len(intact) < min_polymer:
            min_polymer = len(intact)

    return min_polymer

if __name__ == '__main__':
    # - 1 to remove newline
    print find_remains(INPUT_FILE) 
