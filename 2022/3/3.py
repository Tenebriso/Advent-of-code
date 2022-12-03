def _calculate_rucksack_score(items):
    first = set(items[0:len(items) // 2])
    second = set(items[len(items) // 2::])
    return _calculate_common_items_score([first, second])


def _calculate_common_items_score(group):
    diff = set.intersection(*group)
    score = 0
    for item in diff:
        score += _calculate_item_score(item)
    return score


def _calculate_item_score(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 27


def part_one():
    with open('input') as fp:
        total = 0
        for line in fp:
            line = list(line.strip())
            total += _calculate_rucksack_score(line)
        return total


def part_two():
    elf_group_size = 3
    total = 0
    with open('input') as fp:
        group = []
        for idx, line in enumerate(fp, 1):
            group.append(set(list(line.strip())))
            if idx % elf_group_size == 0:
                total += _calculate_common_items_score(group)
                group = []
    return total


if __name__ == '__main__':
    print(f'Part one: {part_one()}')
    print(f'Part two: {part_two()}')
