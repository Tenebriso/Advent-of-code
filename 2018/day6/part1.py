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
    points_to_surface = {}
    max_surface = 0 
    for x in range(min_coords.x, max_coords.x + 1):
        for y in range(min_coords.y, max_coords.y + 1):
            min_distance = 100000
            min_points = []
            for point in coords:
                dist = get_distance(point, Point(x,y))
                if dist == min_distance:
                    min_points.append(point)
                elif dist < min_distance:
                    min_distance = dist
                    min_points = [point]
            if len(min_points) == 1:
                min_point = min_points[0]
                try:
                    points_to_surface[min_point] += 1
                except KeyError:
                    points_to_surface[min_point] = 1
                if min_point.x == min_coords.x or min_point.y == min_coords.y or \
                        min_point.x == max_coords.x or min_point.y == max_coords.y:
                            continue
                if points_to_surface[min_point] > max_surface:
                    max_surface = points_to_surface[min_point]
    return max_surface
    
if __name__ == '__main__':
    print get_distances('input')

