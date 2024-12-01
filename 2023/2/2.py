from functools import reduce


def get_game_power(runs):
    min_game_config = {'red': 0, 'green': 0, 'blue': 0}
    for run in runs:
        run = run.strip().split(',')
        for cube in run:
            number_cubes, color = cube.strip().split(' ')
            number_cubes = int(number_cubes)
            if number_cubes > min_game_config[color]:
                min_game_config[color] = number_cubes
    return reduce(lambda x, y: x * y, min_game_config.values())


total = 0
with open('input') as file_input:
    for line in file_input:
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game_id, runs = line.split(':')
        game_id = int(game_id.split(' ')[1])
        #[ 3 blue, 4 red],[ 1 red, 2 green, 6 blue],[ 2 green]
        runs = runs.strip().split(';')
        game_power = get_game_power(runs)
        total += game_power
print(total)



