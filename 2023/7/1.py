from collections import Counter
from functools import cmp_to_key


CARD_STRENGTH = {
    'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1
}


def get_hand_points(hand):
    occurrences = Counter(hand)
    hand_points = max(occurrences.values())
    # five_of_a_kind or four_of_a_kind
    if hand_points == 5 or hand_points == 4:
        return hand_points + 1
    # high_card
    if hand_points == 1:
        return 0
    if hand_points == 3:
        if len(occurrences) == 2:
            return 4  # full_house
        return 3  # three_of_a_kind
    if len(occurrences) == 3:
        return 2  # two_pair
    return 1  # one_pair


def compare_hands(hand1, hand2):
    hand1_value = get_hand_points(hand1)
    hand2_value = get_hand_points(hand2)
    if hand1_value < hand2_value:
        return -1
    if hand1_value > hand2_value:
        return 1
    return compare_equal_hands(hand1, hand2)


def compare_equal_hands(hand1, hand2):
    for card1, card2 in zip(hand1, hand2):
        if card1 == card2:
            continue
        if CARD_STRENGTH[card1] < CARD_STRENGTH[card2]:
            return -1
        if CARD_STRENGTH[card1] > CARD_STRENGTH[card2]:
            return 1
    return 0


def get_total_winnings(hands):
    total = 0
    hands_ranked = sorted(hands.keys(), key=cmp_to_key(compare_hands))
    for idx, hand in enumerate(hands_ranked):
        card_bid = (idx + 1) * hands[hand]
        total = total + card_bid
        print(f"{hand}")
    return total


hands = {}
with open("input") as input_file:
    for line in input_file:
        hand, bid = line.split()
        hands[hand.strip()] = int(bid)
print(get_total_winnings(hands))

