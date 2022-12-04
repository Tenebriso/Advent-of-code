def check_if_contained(intervals):
    a1, a2, b1, b2 = _interval_heads(intervals)
    if a1 <= b1 and a2 >= b2:
        return True
    if b1 <= a1 and b2 >= a2:
        return True
    return False


def _interval_heads(intervals):
    a1, a2 = [int(x) for x in intervals[0].split('-')]
    b1, b2 = [int(x) for x in intervals[1].split('-')]
    return a1, a2, b1, b2


def check_if_overlapped(intervals):
    a1, a2, b1, b2 = _interval_heads(intervals)
    if a1 <= b1 <= a2:
        return True
    if b1 <= a1 <= b2:
        return True
    return False


def solve(part):
    total = 0
    with open('input') as fp:
        for line in fp:
            line = line.strip().split(',')
            if part == 1 and check_if_contained(line):
                total += 1
            elif part == 2 and check_if_overlapped(line):
                total += 1
    return total


if __name__ == '__main__':
    print(f'Part one: {solve(1)}')
    print(f'Part one: {solve(2)}')


