seeds = []
seeds_range = []
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
            total = [int(x) for x in line[1::]]
            seeds = [x for idx, x in enumerate(total) if idx % 2 == 0]
            seeds_range = [x for idx, x in enumerate(total) if idx % 2 == 1]
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


def break_interval_into_smaller_intervals(start, end):
    
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
for idx, source_seed in enumerate(seeds):
    print(f"on seed {idx} out of {len(seeds)}")
    for diff in range(seeds_range[idx]):
        seed = source_seed + diff
        location = get_location_for_seed(seed)
        if location < min_location:
            min_location = location
print(min_location)
