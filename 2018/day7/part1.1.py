import networkx as nx

INPUT_FILE = 'input'

def generate_graph(filename):
    graph = nx.DiGraph()
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip().split()
            graph.add_edge(line[1], line[-3])
    return graph


def parse_graph(filename):
    graph = generate_graph(filename)
    return nx.lexicographical_topological_sort(graph)


if __name__ == '__main__':
    print "".join(parse_graph(INPUT_FILE))
