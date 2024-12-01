def read_galaxies_pos():
    image = []
    with open("input") as input_file:
        for i, line in enumerate(input_file):
            line = list(line.strip())
            image.append(line)
            # double rows
            if '#' not in set(line):
                image.append(line)
    # double columns
    expanded_galaxy = [[] for _ in image]
    for j in range(len(image[0])):
        for i in range(len(image)):
            expanded_galaxy[i].append(image[i][j])
        column = [image[i][j] for i in range(len(image))]
        if '#' not in set(column):
            for i in range(len(image)):
                expanded_galaxy[i].append(image[i][j])
    # get positions
    galaxies = []
    for i, row in enumerate(expanded_galaxy):
        for j, col in enumerate(row):
            if col == '#':
                galaxies.append((i, j))
    return galaxies


def get_total_distances_between_all_galaxies(galaxies):
    total_distance = 0
    for i, galaxy in enumerate(galaxies[:len(galaxies) - 1]):
        for next_galaxy in galaxies[i+1::]:
            distance = next_galaxy[0] - galaxy[0] + abs(next_galaxy[1] - galaxy[1])
            total_distance += distance
    return total_distance


galaxies = read_galaxies_pos()
print(get_total_distances_between_all_galaxies(galaxies))