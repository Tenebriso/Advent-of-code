firewall = {}


def reader(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()


def build_firewall(filename):
    r = reader(filename)
    while True:
        try:
            words = map(int, r.next().split(': '))
            firewall[words[0]] = words[1]
        except StopIteration:
            break


def traverse_firewall():
    severity = 0
    end = max(firewall.keys())
    step = 0
    for step in range(end + 1):
        if step not in firewall:
            continue
        else:
            current = step
            depth = firewall[step] - 1
            while current >= 2 * depth:
                current -= 2 * depth
            if current == 0:
                severity += step * (depth + 1)
    return severity


if __name__ == '__main__':
    build_firewall('input_file')
    print firewall
    print(traverse_firewall())
