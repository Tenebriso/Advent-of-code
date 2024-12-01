total = 0
with open("input") as input_file:
    for line in input_file:
        points = -1
        cards = line.strip().split(":")[1].strip().split("|")
        winning_cards = set([int(x) for x in cards[0].strip().split()])
        own_cards = set([int(x) for x in cards[1].strip().split()])
        for number in own_cards:
            if number in winning_cards:
                points += 1
        if points >= 0:
            total += 2 ** points
print(total)
