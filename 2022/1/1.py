import heapq


def find_max():
    max_cals = 0
    with open('input') as fp:
        current_cals = 0
        for line in fp:
            line = line.strip()
            if not line:
                if max_cals < current_cals:
                    max_cals = current_cals
                current_cals = 0
            else:
                current_cals += int(line)
    return max_cals


def find_max_three():
    all_calories = []
    with open('input') as fp:
        current_cals = 0
        for line in fp:
            line = line.strip()
            if not line:
                all_calories.append(current_cals)
                current_cals = 0
            else:
                current_cals += int(line)
    return heapq.nlargest(3, all_calories)


if __name__ == '__main__':
    print("Part 1: " + str(find_max()))
    print("Part 2: " + str(sum(find_max_three())))