l = [x for x in range(256)]


def reader(filename):
    with open(filename) as f:
        lengths = f.read().split(',')
    for length in lengths:
        yield length

def reverse_portion(current_pos, length):
    if current_pos >= len(l):
        current_pos %= len(l)
    if current_pos < 0:
        current_pos += len(l) - 1
    final_pos = current_pos + length - 1
    if final_pos >= len(l):
        final_pos %= len(l)
    new_current_pos = final_pos
    for i in range(length/2):
        aux = l[final_pos]
        l[final_pos] = l[current_pos]
        l[current_pos] = aux
        current_pos += 1
        final_pos -= 1
        if final_pos < 0:
            final_pos = len(l) - 1
        if current_pos >= len(l):
            current_pos = 0
    return new_current_pos

if __name__ == '__main__':
    r = reader('input_file')
    skip = 0
    current_pos = 0
    while True:
        try:
            length = int(r.next())
            current_pos = reverse_portion(current_pos, length) + skip + 1
            skip += 1
        except StopIteration:
            break
    print(l)
    print(l[0] * l[1])
