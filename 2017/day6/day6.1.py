def count_cycles(blocks):
    count = 0
    seen_states = set()
    while True:
        max_val = max(blocks)
        max_idx = blocks.index(max_val)
        blocks[max_idx] = 0
        start = max_idx + 1 if max_idx + 1< len(blocks) else 0
        while max_val > 0:
            blocks[start] += 1
            max_val -= 1
            start = start + 1 if start + 1 < len(blocks) else 0
        count += 1
        current_state = tuple(blocks)
        if current_state in seen_states:
            return count
        else:
            seen_states.add(current_state)

if __name__ == '__main__':
    with open('input_file') as f:
        blocks = map(int, f.read().split())
    print(count_cycles(blocks))

