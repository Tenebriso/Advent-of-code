def get_card_points(winning_numbers, own_numbers):
    points = 0
    for number in own_numbers:
        if number in winning_numbers:
            points += 1
    return points


def update_duplicate_cards(current_index, points, duplicate_cards):
    copies_to_add = 1
    if current_index in duplicate_cards:
        copies_to_add = duplicate_cards[current_index] + 1
    for i in range(current_index + 1, current_index + points + 1):
        if i in duplicate_cards:
            duplicate_cards[i] += copies_to_add
        else:
            duplicate_cards[i] = copies_to_add
    return duplicate_cards


with open("input") as input_file:
    duplicate_cards = {}
    for card_number, line in enumerate(input_file):
        cards = line.strip().split(":")[1].strip().split("|")
        winning_numbers = set([int(x) for x in cards[0].strip().split()])
        own_numbers = set([int(x) for x in cards[1].strip().split()])
        points = get_card_points(winning_numbers, own_numbers)
        duplicate_cards = update_duplicate_cards(card_number + 1, points, duplicate_cards)
        # count the originals too
        if card_number + 1 in duplicate_cards:
            duplicate_cards[card_number + 1] += 1
        else:
            duplicate_cards[card_number + 1] = 1


print(sum(duplicate_cards.values()))
