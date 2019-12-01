INPUT_FILE = 'input'

def read_marbles():
    with open(INPUT_FILE) as marble_file:
        line = marble_file.readline().strip().split()
    return int(line[0]), int(line[-2])


def compute_score(nb_players, nb_marbles):
    players_score = {x: 0 for x in range(nb_players)}
    circle = [0]
    current_marble = 0
    player = 0
    for marble in range(1, nb_marbles):
        player = (player + 1) % nb_players
        if marble % 23 == 0:
            rm_marble = (current_marble - 7) % len(circle)
            players_score[player] += circle[rm_marble] + marble
            del circle[rm_marble]
            current_marble = rm_marble
        else:
            m1 = (current_marble + 1) % len(circle)
            m2 = (current_marble + 2) % len(circle)
            if m2 <= m1:
                circle.append(marble)
                current_marble = m1 + 1
            else:
                circle.insert(m2, marble)
                current_marble = m2 
    return players_score


if __name__ == '__main__':
    nb_players, nb_marbles = read_marbles()
    print max(compute_score(nb_players, nb_marbles).values())


