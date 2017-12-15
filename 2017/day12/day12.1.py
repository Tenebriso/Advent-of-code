village = {}


def reader(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()


def build_village(line):
    line = line.split(' <-> ')
    neighbors = line[1].split(', ')
    for neighbor in neighbors:
        try:
            village[line[0]].append(neighbor)
        except KeyError:
            village[line[0]] = [neighbor]


def find_group_zero():
    visited = set()
    group0 = ['0']
    while group0:
        v = group0.pop()
        for neighbor in village[v]:
            if neighbor not in visited:
                group0.append(neighbor)
        visited.add(v)
    return len(visited)


if __name__ == '__main__':
    r = reader('input_file')
    while True:
        try:
            line = r.next()
        except StopIteration:
            break
        build_village(line)
    print(find_group_zero())
