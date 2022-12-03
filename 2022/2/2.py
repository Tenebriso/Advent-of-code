wins = [('B', 'Z'), ('A', 'Y'), ('C', 'X')]
draws = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
loses = [('A', 'Z'), ('B', 'X'), ('C', 'Y')]
outcomes_to_moves = {'X': dict(loses), 'Y': dict(draws), 'Z': dict(wins)}
points = {'X': 1, 'Y': 2, 'Z': 3}


def _calculate_round_score(enemy_move, my_move):
    score = points[my_move]
    if (enemy_move, my_move) in wins:
        score += 6
    elif (enemy_move, my_move) in draws:
        score += 3
    return score


def part_one():
    score = 0
    with open('input') as fp:
        for line in fp:
            enemy_move, my_move = line.strip().split()
            score += _calculate_round_score(enemy_move, my_move)
    return score


def part_two():
    score = 0
    with open('input') as fp:
        for line in fp:
            enemy_move, outcome = line.strip().split()
            my_move = outcomes_to_moves[outcome][enemy_move]
            score += _calculate_round_score(enemy_move, my_move)
    return score


if __name__ == '__main__':
    print(f"Part 1: {part_one()}")
    print(f"Part 2: {part_two()}")
