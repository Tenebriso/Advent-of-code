CONFIG = {'red': 12, 'green':13, 'blue': 14 }


def is_game_possible(runs):
    for run in runs:
        run = run.strip().split(',')
        for cube in run:
            number_cubes, color = cube.strip().split(' ')
            if int(number_cubes) > CONFIG[color]:
                return False
    return True


total = 0
with open('input') as file_input:
    for line in file_input:
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game_id, runs = line.split(':')
        game_id = int(game_id.split(' ')[1])
        #[ 3 blue, 4 red],[ 1 red, 2 green, 6 blue],[ 2 green]
        runs = runs.strip().split(';')
        if is_game_possible(runs):
            total += game_id
print(total)



