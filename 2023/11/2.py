import collections

galaxy = collections.namedtuple('galaxy', 'galaxies_pos empty_rows empty_cols')
OFFSET = 10


def read_galaxies_pos():
    image = []
    galaxies_pos = []
    empty_rows = set()
    empty_cols = set()
    with open("input") as input_file:
        for i, line in enumerate(input_file):
            line = list(line.strip())
            image.append(line)
            if '#' not in set(line):
                empty_rows.add(i)
                continue
            for j, val in enumerate(line):
                if val == '#':
                    galaxies_pos.append((i, j))
    # empty columns
    for j in range(len(image[0])):
        column = [image[i][j] for i in range(len(image))]
        if '#' not in set(column):
            empty_cols.add(j)
    return galaxy(galaxies_pos, empty_rows, empty_cols)


def get_total_distances_between_all_galaxies(galaxies):
    total_distance = 0
    for i, current_galaxy in enumerate(galaxies.galaxies_pos[:len(galaxies) - 1]):
        for next_galaxy in galaxies.galaxies_pos[i+1::]:
            current_i = current_galaxy[0] if current_galaxy[0] not in galaxies.empty_rows else current_galaxy[0] + OFFSET
            current_j = current_galaxy[1] if current_galaxy[1] not in galaxies.empty_cols else current_galaxy[1] + OFFSET
            next_i = next_galaxy[0] if next_galaxy[0] not in galaxies.empty_rows else next_galaxy[0] + OFFSET
            next_j = next_galaxy[1] if next_galaxy[1] not in galaxies.empty_cols else next_galaxy[1] + OFFSET
            distance = next_i - current_i + abs(next_j - current_j)
            total_distance += distance
    return total_distance


galaxies = read_galaxies_pos()
print(galaxies)
print(get_total_distances_between_all_galaxies(galaxies))

latest_intent_of_order = dict()
entries_with_different_autofit = latest_intent_of_order[(latest_intent_of_order['reverse_geocode_address_short'].notnull() & (((latest_intent_of_order['gps_lat'] != latest_intent_of_order['previous_location_lat']) | (latest_intent_of_order['gps_lng'] != latest_intent_of_order['previous_location_lng'])) & (latest_intent_of_order['reverse_geocode_address_short'] != latest_intent_of_order['previous_location_address_short'])) & (latest_intent_of_order['delivery_address_source'] != 'auto_switch_location'))]
