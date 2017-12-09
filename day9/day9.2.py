def reader(filename):
    with open(filename) as f:
        while True:
            character = f.read(1)
            if character:
                yield character
            else:
                break


def process_line(filename):
    r = reader(filename)
    stack = []
    total = 0
    skip = False
    while True:
        try:
            letter = r.next()
        except StopIteration:
            break
        # Check to skip
        if skip:
            skip = False
            continue
        if letter == '!':
            skip = True
            continue
        if not skip:
            if not stack:
                if letter == '<':
                       stack.append(letter)
                continue
            # In garbage
            if stack[len(stack) - 1] == '<':
                if letter == '>':
                    stack.pop()
                else:
                    total += 1
            # Start of garbage
            elif letter == '<':
                stack.append(letter)
    return total

if __name__ == '__main__':
    print(process_line('input_file'))

