def find_marker_index(line, marker_length):
    marker = []
    for idx, character in enumerate(line):
        try:
            index = marker.index(character)
            marker = marker[index + 1::]
        except ValueError:
            pass
        marker.append(character)
        if len(marker) == marker_length:
            return idx + 1


def solve(part):
    marker_length = 4 if part == 1 else 14
    with open("input") as fp:
        for line in fp:
            return find_marker_index(line.strip(), marker_length)


print(f"Part one: {solve(1)}")
print(f"Part one: {solve(2)}")
