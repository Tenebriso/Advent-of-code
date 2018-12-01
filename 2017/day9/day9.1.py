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
        # Check skip
        if skip:
            skip = False
            continue
        if letter == '!':
            skip = True
            continue
        if not skip:
            # Empty stack
            if not stack:
                if letter == '<' or \
                   letter == '{':
                       stack.append(letter)
                       total += stack.count('{')
                continue
            # In garbage
            if stack[len(stack) - 1] == '<':
                if letter == '>':
                    stack.pop()
            # Start of garbage
            elif letter == '<':
                stack.append(letter)
            # Start of group
            elif letter == '{':
                stack.append(letter)
                total += stack.count('{')
            # End of group
            elif letter == '}':
                stack.pop()
    return total

if __name__ == '__main__':
    print(process_line('input_file'))

