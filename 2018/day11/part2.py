SERIAL =8561 
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


def grid_power(x, y, size):
    total_power = 0
    for i in range(y, y + size):
        for j in range(x, x + size):
            total_power += cell_power(j, i)
    return total_power


def parse_grid():
    max_power = -100000
    top_left = (0, 0)
    grid_size = 0
    summed_area = [[0] * 301 for _ in range(301)]
    for x in range(1, X + 1):
        for y in range(1, Y + 1):
            summed_area[x][y] = cell_power(x,y) + summed_area[x-1][y] + summed_area[x][y-1] - summed_area[x - 1][y - 1]
    for size in range(1, 300):
        for i in range(1, Y - size + 1):
            for j in range(1, X - size + 1):
                # i(x,y)=I(D)+I(A)-I(B)-I(C)
                power = summed_area[j + size][i + size] - summed_area[j][i + size] \
                         -summed_area[j + size][i] + summed_area[j][i]
                if power > max_power:
                    max_power = power
                    grid_size = size
                    top_left = (j + 1, i + 1)
            
    return top_left, grid_size


if __name__ == '__main__':
    print parse_grid()
