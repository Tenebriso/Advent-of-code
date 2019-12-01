SERIAL = 8561
X = 300
Y = 300


def cell_power(x, y):
    '''
    Find the fuel cell's rack ID, which is its X coordinate plus 10.
    Begin with a power level of the rack ID times the Y coordinate.
    Increase the power level by the value of the grid serial number (your puzzle input).
    Set the power level to itself multiplied by the rack ID.
    Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
    Subtract 5 from the power level.
    '''
    rack_id = x + 10
    power = rack_id * y + SERIAL
    power *= rack_id
    power = (power / 100 % 10) - 5
    return power


def grid_power(x, y):
    first_row = cell_power(x-1, y) + cell_power(x-1, y - 1) + cell_power(x-1, y+1)
    second_row = cell_power(x, y) + cell_power(x, y - 1) + cell_power(x, y+1)
    third_row = cell_power(x+1, y) + cell_power(x+1, y - 1) + cell_power(x+1, y+1)
    return first_row + second_row + third_row


def parse_grid():
    max_power = -100000
    top_left = (0, 0)
    for i in range(2, Y):
        for j in range(2, X):
            power = grid_power(j, i)
            if power > max_power:
                max_power = power
                top_left = (j-1, i-1)
    return max_power, top_left


if __name__ == '__main__':
    print parse_grid()
