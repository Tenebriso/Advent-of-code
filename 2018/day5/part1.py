INPUT_FILE = 'input'

def letter_generator(filename):
    with open(filename) as input_file:
        char = input_file.read(1)
        while char:
            yield char
            char = input_file.read(1)


def find_remains(filename):
    char_gen = letter_generator(filename)
    intact = []
    while True:
        try:
            letter = next(char_gen)
            if intact:
                intact.append(letter)
                continue
            if intact[-1] != letter and intact[-1].lower() == letter.lower():
                   intact.pop()
            else:
                intact.append(letter)
        except StopIteration:
            break
    return intact

if __name__ == '__main__':
    # - 1 to remove newline
    print len(find_remains(INPUT_FILE)) - 1
