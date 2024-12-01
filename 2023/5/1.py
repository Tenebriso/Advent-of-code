seeds = []
transformations = {}
maps = {}

with open("input") as input_file:
    current_source = ""
    for line in input_file:
        line = line.strip().split()
        # empty line
        if not line:
            continue
        # seeds
        if line[0] == "seeds:":
            seeds = [int(x) for x in line[1::]]
            continue
        # map title
        if line[1] == "map:":
            line = line[0].split("-")
            current_source = line[0]
            transformations[current_source] = line[2]
            maps[current_source] = {}
            continue
        # mappings
        line = [int(x) for x in line]
        maps[current_source][line[1]] = (line[0], line[2])


def get_location_for_seed(seed):
    source_type = "seed"
    source_value = seed
    while True:
        try:
            source_to_destination = maps[source_type]
        except KeyError:
            return source_value
        found_mapping = False
        for source, destination in source_to_destination.items():
            if source_value >= source:
                if source_value < source + destination[1]:
                    found_mapping = True
                    source_type = transformations[source_type]
                    source_value = destination[0] + (source_value - source)
                    # probably found location
                    if source_type not in transformations:
                        return source_value
                    break
        # keep the same value if no destination matches
        if not found_mapping:
            source_type = transformations[source_type]


min_location = float("inf")
for seed in seeds:
    location = get_location_for_seed(seed)
    if location < min_location:
        min_location = location
print(min_location)
