from collections import deque


def read_stacks(fp):
    stacks = {}
    for line in fp:
        pos = 0
        while not line[1].isdigit():
            try:
                val = line[pos * 3 + pos + 1]
                if val.isalpha():
                    if (pos + 1) not in stacks:
                        stacks[pos + 1] = deque([line[pos * 3 + pos + 1]])
                    else:
                        stacks[pos + 1].appendleft(line[pos * 3 + pos + 1])
                pos += 1
            except IndexError:
                break
        else:
            return stacks


def _parse_instruction(instruction):
    instruction = instruction.strip().split()
    quantity = int(instruction[1])
    from_stack = int(instruction[3])
    to_stack = int(instruction[5])
    return quantity, from_stack, to_stack


def read_instructions(fp):
    for line in fp:
        if line.startswith("move"):
            yield _parse_instruction(line)


def apply_instruction_single_crate(stacks, quantity, from_stack, to_stack):
    for i in range(quantity):
        stacks[to_stack].append(stacks[from_stack].pop())


def apply_instruction_multiple_crates(stacks, quantity, from_stack, to_stack):
    crane_holds = deque()
    for i in range(quantity):
        crane_holds.append(stacks[from_stack].pop())
    while crane_holds:
        stacks[to_stack].append(crane_holds.pop())


def read_tops(stacks):
    tops = []
    for i in range(1, len(stacks) + 1):
        tops.append(stacks[i].pop())
    return tops


def solve(part):
    with open("input") as fp:
        stacks = read_stacks(fp)
        for instruction in read_instructions(fp):
            if part == 1:
                apply_instruction_single_crate(stacks, *instruction)
            elif part == 2:
                apply_instruction_multiple_crates(stacks, *instruction)
    return read_tops(stacks)


print(f"Part one = {''.join(solve(1))}")
print(f"Part two= {''.join(solve(2))}")
