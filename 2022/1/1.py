import heapq


def find_max_n(n=1):
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
    return heapq.nlargest(n, all_calories)


if __name__ == '__main__':
    print("Part 1: " + str(sum(find_max_n())))
    print("Part 2: " + str(sum(find_max_n(3))))
