from collections import defaultdict

INPUT_FILE = 'input'

def read_input(filename):
    dependency_graph = defaultdict(set)
    all_nodes = set()
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip().split()
            dependency_graph[line[-3]].add(line[1])
            all_nodes.add(line[-3])
            all_nodes.add(line[1])
    return dependency_graph, all_nodes

def parse_graph(filename):
    graph, all_nodes = read_input(filename)
    all_nodes = sorted(all_nodes)
    solved = []
    visited = set(solved)
    idx = 0 
    while idx < len(all_nodes):
        node = all_nodes[idx]
        if node in visited:
            idx += 1
            continue 
        unsolved_dependencies = graph[node] - set(solved)
        if not unsolved_dependencies:
            solved.append(node)
            visited.add(node)
            idx = 0
        else:
            idx += 1
    return solved


if __name__ == '__main__':
    print "".join(parse_graph(INPUT_FILE))

