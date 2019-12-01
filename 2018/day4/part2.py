from datetime import datetime
from collections import defaultdict, Counter

INPUT_FILE = 'input'


def read_input(filename):
    time_to_action = {}
    with open(filename) as input_file:
        for line in input_file:
            line = line.split()
            time = datetime.strptime((line[0]+ " " +line[1])[1:-1], "%Y-%m-%d %H:%M")
            time_to_action[time] = " ".join(line[2:])
    return sorted(time_to_action), time_to_action


def detect_max(filename):
    time, time_to_action = read_input(filename)
    id_to_minutes = defaultdict(dict)
    sleepiest_minute = None
    sleepiest_guard = None
    max_minutes = 0
    guard_id = 0
    for moment in time:
        action = time_to_action[moment]
        if action == 'falls asleep':
            start_time = moment.minute
        elif action == 'wakes up':
            end_time = moment.minute
            for minute in range(start_time, end_time):
                try:
                    id_to_minutes[guard_id][minute] += 1
                    if max_minutes < id_to_minutes[guard_id][minute]:
                        max_minutes = id_to_minutes[guard_id][minute]
                        sleepiest_minute = minute
                        sleepiest_guard = guard_id
                except KeyError:
                        id_to_minutes[guard_id][minute] = 1
        else:
            guard_id = int(action[7:11])
    return sleepiest_minute * sleepiest_guard

if __name__ == '__main__':
    print detect_max(INPUT_FILE)
