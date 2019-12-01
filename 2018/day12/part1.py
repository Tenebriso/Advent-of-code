GENERATIONS = 20
INPUT_FILE = 'input'

def parse_input():
    growing_rules = {}
    with open(INPUT_FILE) as plants:
        initial_state = plants.readline().split()[2]
        plants.readline()
        for line in plants:
            line = line.split()
            growing_rules[line[0]] = line[2]

    return initial_state, growing_rules


def compute_next_generation(initial_config, growing_rules):
    shift = 0
    new_config = '..'
    if growing_rules['....' + initial_config[0:1]] == '#':
        new_config += '#'
        shift += 1
    if growing_rules['...' + initial_config[0:2]] == '#':
        new_config += '#'
        shift += 1
    if growing_rules['..' + initial_config[0:3]] == '#':
        new_config += '#'
        shift += 1
    if growing_rules['.' + initial_config[0:4]] == '#':
        new_config += '#'
        shift += 1
    for i in range(2, len(initial_config) - 2):
        llcrr = initial_config[i-2:i+3]
        new_config += growing_rules[llcrr]
    if growing_rules[initial_config[-4:] + '.'] == '#':
        new_config += '#'
    if growing_rules[initial_config[-3:] + '..'] == '#':
        new_config += '#'
    if growing_rules[initial_config[-2:] + '...'] == '#':
        new_config += '#'
    if growing_rules[initial_config[-1:] + '....'] == '#':
        new_config += '#'
    new_config += '..'
    return new_config, shift


def compute_final(initial_config, growing_rules):
    shift = 0
    from collections import OrderedDict
    seen_config = OrderedDict()
    for generation in range(GENERATIONS):
        first = initial_config.find('#')
        last = initial_config.rfind('#')
        valid_slice = initial_config[first: last+1]
        if valid_slice in seen_config:
            left_gens = GENERATIONS - generation
            current_index = seen_config.keys().index(valid_slice)
            break
        seen_config[valid_slice] = shift
        new_config, new_shift = compute_next_generation(initial_config, growing_rules)
        shift += new_shift
        initial_config = new_config
    keys = seen_config.keys()
    the_s = 0
    for i in range(current_index, len(seen_config)):
            the_s += seen_config[keys[i]]
    print left_gens * the_s
    shift += left_gens * the_s
    print shift
    '''
    last = new_config.rfind('#')
    tot = 0
    mock_shift = 0 - shift - 2
    for pot in range(0, last + 1):
        if initial_config[pot] == '#':
            tot += mock_shift
        mock_shift += 1
    print tot
    '''


if __name__ == '__main__':
    initial_config, growing_rules =  parse_input()
    compute_final('..' + initial_config + '..' , growing_rules)

