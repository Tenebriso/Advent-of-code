import json
from functools import cmp_to_key


def compare(packet1, packet2):
    for i in range(len(packet1)):
        check = 0
        if i == len(packet2):
            return 1
        if type(packet1[i]) == int and type(packet2[i]) == int:
            if packet2[i] < packet1[i]:
                return 1
            if packet1[i] < packet2[i]:
                return -1
        elif type(packet1[i]) == int and type(packet2[i]) == list:
            check = compare([packet1[i]], packet2[i])
        elif type(packet1[i]) == list and type(packet2[i]) == int:
            check = compare(packet1[i], [packet2[i]])
        if type(packet1[i]) == list and type(packet2[i]) == list:
            check = compare(packet1[i], packet2[i])
        if check != 0:
            return check
    # empty packet1
    if len(packet1) < len(packet2):
        return -1
    # inconclusive
    return 0


def read_packets():
    total = 0
    i = 0
    lines = []
    with open('input', 'r') as fp:
        for line in fp:
            i += 1
            if not line.strip():
                line = fp.readline()
            second_line = fp.readline()
            packet1 = json.loads(line)
            packet2 = json.loads(second_line)
            lines.extend([packet1, packet2])
            check = compare(packet1, packet2)
            if check < 1:
                total += i
    return total, lines


def solve():
    total, lines = read_packets()
    divider1, divider2 = [[2]], [[6]]
    lines.extend([divider1, divider2])
    print(f"Part one = {total}")
    sorted_packets = sorted(lines, key=cmp_to_key(compare))
    print(f"Part two = {(sorted_packets.index(divider1) + 1) * (sorted_packets.index(divider2) + 1)}")


solve()
