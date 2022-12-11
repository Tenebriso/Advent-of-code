import math
import time
from collections import deque


monkeys = {}


class Monkey:
    def __init__(self, monkey_id, items, operation, test):
        self.id = monkey_id
        self.items = items
        self.operation = operation
        self.test = test
        self.inspected_items = 0

    def inspect_item(self, item, part, worry_reducer):
        item_to_throw = reduce_worry(self.apply_operation(item), part, worry_reducer)
        other_monkey = self.test[item_to_throw % self.test['value'] == 0]
        throw_to_monkey(item_to_throw, other_monkey)
        self.inspected_items += 1

    def apply_operation(self, item):
        operation = self.operation.replace("old", str(item))
        return eval(operation)

    def inspect_items(self, part, worry_reducer):
        while self.items:
            self.inspect_item(self.items.pop(), part, worry_reducer)

    def __str__(self):
        return f"Monkey {self.id}: {self.inspected_items}"


def throw_to_monkey(item, other_monkey):
    monkeys[other_monkey].items.append(item)


def reduce_worry(item, part, worry_reducer):
    if part == 1:
        return item // 3
    elif part == 2:
        return item % worry_reducer


def read_monkeys():
    monkeys = {}
    items = deque()
    operation = ''
    test = {'value': None, True: None, False: None}
    monkey_id = None
    with open('input') as fp:
        for line in fp:
            line = line.strip()
            if line.startswith("Monkey"):
                monkey_id = int(line.strip().split()[1].replace(":", ""))
            elif line.startswith("Starting"):
                items = [int(item) for item in line.split(':')[1].split(',')]
            elif line.startswith('Operation'):
                operation = line.split('=')[1].strip()
            elif line.startswith("Test"):
                test['value'] = int(line.split()[-1])
            elif line.startswith("If true"):
                test[True] = int(line.split()[-1])
            elif line.startswith("If false"):
                test[False] = int(line.split()[-1])
            else:
                monkeys[monkey_id] = Monkey(monkey_id=monkey_id, items=items, operation=operation, test=test.copy())
        # last monkey
        monkeys[monkey_id] = Monkey(monkey_id=monkey_id, items=items, operation=operation, test=test.copy())
    return monkeys


def play(rounds, part):
    worry_reducer = 3
    if part == 2:
        worry_reducer = math.prod([int(x.test['value']) for x in monkeys.values()])
    for i in range(rounds):
        for monkey in monkeys.values():
            monkey.inspect_items(part, worry_reducer)


def solve(part, rounds=20, most_active_count=2):
    global monkeys
    monkeys = read_monkeys()
    play(rounds, part)
    return math.prod(sorted([x.inspected_items for x in monkeys.values()], reverse=True)[:most_active_count])


print(f"Part one = {solve(1, 20)}")
print(f"Part two = {solve(2, 10000)}")
