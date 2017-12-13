l = [x for x in range(256)]
base = [17, 31, 73, 47, 23]

def reader(filename):
    lengths = []
    with open(filename) as f:
        while True:
            length = f.read(1)
            if not length or length == '\n':
                break
            lengths.append(ord(length))
    lengths += base
    return lengths

def reverse_portion(current_pos, length):
    if current_pos >= len(l):
        current_pos %= len(l)
    if current_pos < 0:
        current_pos += len(l) - 1
    final_pos = current_pos + length - 1
    if final_pos >= len(l):
        final_pos %= len(l)
    new_current_pos = final_pos
    for _i in range(length/2):
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


def sparse_to_dense():
    block_count = 0
    dense = [0] * 16
    for number in l:
        if block_count == 16:
            block_count = 0
        dense[block_count] ^= number
        block_count += 1
    return dense


def int_to_hex(dense):
    hexes = []
    for number in dense:
        hexes.append("%0.2X".lower() % number)
    return hexes

if __name__ == '__main__':
    lengths = reader('input_file')
    skip = 0
    current_pos = 0
    for _i in range(64):
        for length in lengths:
            current_pos = reverse_portion(current_pos, length) + skip + 1
            skip += 1
    print(''.join(int_to_hex(sparse_to_dense())))
    '''
    while True:
        try:
            length = int(r.next())
        except StopIteration:
            break
    print(l[0] * l[1])
    '''
