from collections import namedtuple

INPUT_FILE = 'input'

Point = namedtuple('Point', ['x', 'y'])

def read_input(filename):
    coords = []
    max_coords = Point(0, 0)
    min_coords = Point(1000, 1000)
    with open(filename) as points:
        for line in points:
            point = map(int, line.strip().split(', '))
            coords.append(Point(point[0], point[1]))
            if point[0] < min_coords.x:
                min_coords = Point(point[0], min_coords.y)
            if point[1] < min_coords.y:
                min_coords = Point(min_coords.x, point[1])
            if point[1] > max_coords.y:
                max_coords = Point(max_coords.x, point[1])
            if point[0] > max_coords.x:
                max_coords = Point(point[0], max_coords.y)
    return sorted(coords), min_coords, max_coords


def get_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)
 

def get_distances(filename):
    coords, min_coords, max_coords = read_input(filename)
    points = 0
    max_surface = 0 
    for x in range(min_coords.x, max_coords.x + 1):
        for y in range(min_coords.y, max_coords.y + 1):
            total_distance = 0
            for point in coords:
                dist = get_distance(point, Point(x,y))
                total_distance += dist
                if total_distance >= 10000:
                    break
            if total_distance < 10000:
                points += 1

    return points
    
if __name__ == '__main__':
    print get_distances('input')

