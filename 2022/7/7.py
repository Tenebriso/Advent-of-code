class Node:
    def __init__(self, value, parent):
        self.parent = parent
        self.value = value
        self.children = []
        self.size = 0

    def add_child(self, child):
        self.children.append(child)

    def get_full_size(self):
        if not self.children:
            return self.size
        for child in self.children:
            self.size += child.get_full_size()
        return self.size


def build_tree():
    current_node = None
    head = None
    with open("input") as fp:
        for line in fp:
            line = line.strip().split()
            if line[0] == '$':
                if line[1] == 'cd':
                    if line[2] == '..':
                        current_node = current_node.parent
                    else:
                        new_node = Node(line[2], current_node)
                        if current_node:
                            current_node.add_child(new_node)
                        current_node = new_node
                        if not head:
                            head = current_node
            elif line[0] != 'dir':
                current_node.size += int(line[0])
    return head


def get_total_nodes_sizes_smaller_than(max_value, head):
    q = [head]
    total = 0
    while q:
        node = q.pop()
        if node.size < max_value:
            total += node.size
        for child in node.children:
            q.append(child)
    return total


def get_free_space(filsystem_size, needed_size, head):
    return needed_size - (filsystem_size - head.size)


def dir_size_to_delete(head, min_size, current_dir_size):
    if min_size <= head.size < current_dir_size:
        current_dir_size = head.size
    for child in head.children:
        children_min = dir_size_to_delete(child, min_size, current_dir_size)
        if children_min < current_dir_size:
            current_dir_size = children_min
    return current_dir_size


def solve(part):
    head = build_tree()
    head.get_full_size()
    if part == 1:
        return get_total_nodes_sizes_smaller_than(100000, head)
    else:
        free_space = get_free_space(70000000, 30000000, head)
        return dir_size_to_delete(head, free_space, head.size)


print(f"Part one = {solve(1)}")
print(f"Part two = {solve(2)}")



