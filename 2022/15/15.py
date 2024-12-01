def manhattan_distance(sensor, beacon):
    dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    return dist


def beacon_on_x(sensor, y, min_distance):
    no_beacons = set()
    # to the left
    x = sensor[0]
    while manhattan_distance(sensor, (x, y)) <= min_distance:
        no_beacons.add((x, y))
        x -= 1
    # to the right
    x = sensor[0]
    while manhattan_distance(sensor, (x, y)) <= min_distance:
        no_beacons.add((x, y))
        x += 1
    return no_beacons


def extract_sensor_beacon_from_line(line):
    sensor = line[0].split(',')
    beacon = line[1].split(',')
    sensor = int(sensor[0].split('=')[1]), int(sensor[1].split('=')[1])
    beacon = int(beacon[0].split('=')[1]), int(beacon[1].split('=')[1])
    return sensor, beacon


def part_one():
    total = set()
    y = 2000000
    with open('input') as fp:
        for line in fp:
            line = line.strip().split(':')
            sensor, beacon = extract_sensor_beacon_from_line(line)
            total = total.union(beacon_on_x(sensor, y, manhattan_distance(sensor, beacon)))
            if beacon in total:
                total.remove(beacon)
    return len(total)


def find_first_possible_beacon(sensor, min_distance, y):
    lo = 0
    hi = sensor[0]
    print(f"Sensor {sensor}: ")
    while hi - lo > 1:
        mid = (hi + lo) // 2
        print(f"\t\tmid = {mid}")
        if manhattan_distance(sensor, (mid, y)) < min_distance:
            print(f"\t\tcan be even lower")
            hi = mid
        else:
            print(f"\t\tshould be higher")
            lo = mid + 1

    if manhattan_distance(sensor, (lo, y)) < min_distance:
        return -1
    if manhattan_distance(sensor, (hi, y)) > min_distance:
        return hi
    return lo


def count_non_beacons_on_y(sensors, limits):
    for y in range(limits[0], limits[1] + 1):
        leftest = limits[1] + 1
        for sensor, beacon in sensors.items():
            left = find_first_possible_beacon(sensor, manhattan_distance(sensor, beacon), y)
            print(f"On {y}, for {sensor}, leftmost possible beacon is: {left}")
            if left < leftest:
                leftest = left
            if leftest == -1:
                break
        print(f"On {y} leftest beacon could be {leftest}")


def part_two():
    sensor_to_beacon = {}
    limits = (0, 20)
    with open('input') as fp:
        for line in fp:
            line = line.strip().split(':')
            sensor, beacon = extract_sensor_beacon_from_line(line)
            sensor_to_beacon[sensor] = beacon
    count_non_beacons_on_y(sensor_to_beacon, limits)

part_two()
