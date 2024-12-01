'''
PART 1
'''
def read_lists(input_file):
    list_a, list_b = [], []
    with open(input_file) as fs:
        for line in fs:
            a, b = line.strip().split()
            list_a.append(int(a))
            list_b.append(int(b))
    return list_a, list_b

def calculate_distance(a, b):
    return abs(a-b)

def calculate_list_distance(list_a, list_b):
    distance = 0
    for idx in range(len(list_a)):
        a = list_a[idx]
        b = list_b[idx]
        distance += calculate_distance(a, b)
    return distance

def part_1():
    list_a, list_b = read_lists("1.input")
    list_a.sort()
    list_b.sort()
    print(calculate_list_distance(list_a, list_b))
part_1()


'''
PART 2
'''
def read_lists_with_occurances(input_file):
    list_a, map_b = [], {}
    with open(input_file) as fs:
        for line in fs:
            a, b = line.strip().split()
            list_a.append(int(a))
            b = int(b)
            if b in map_b:
                map_b[b] += 1
            else:
                map_b[b] = 1
    return list_a, map_b

def calculate_similarity(a, b):
    return a * b

def calculate_lists_similarity(list_a, map_b):
    similarity = 0
    for a in list_a:
        occ_in_b = map_b.get(a) or 0
        similarity += calculate_similarity(a, occ_in_b)
    return similarity

def part_2():
    list_a, map_b = read_lists_with_occurances("1.input")
    print(calculate_lists_similarity(list_a, map_b))
part_2()
