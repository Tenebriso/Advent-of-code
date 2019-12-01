INPUT_FILE = 'input'

class Node:
    def __init__(self,nb_nodes, nb_meta):
        self.nb_nodes = nb_nodes
        self.nb_meta = nb_meta
        self.nodes = []
        self.metadata = []
    def __repr__(self):
        return "({} {})".format(self.nb_nodes, self.nb_meta)
    

def generate_tree():
    with open(INPUT_FILE) as tree_file:
        for line in tree_file:
            line = map(int, line.strip().split())
            tree = generate_helper(line)[0]
            # print_tree(tree)
    return tree
 

def print_tree(tree):
    if tree:
        print "({} {}): {} {}".format(tree.nb_nodes, tree.nb_meta, tree.nodes, tree.metadata)
    for node in tree.nodes:
        print_tree(node)


def sum_metadata(tree, total):
    if tree:
        meta = sum(tree.metadata)
        total += meta
    for child in tree.nodes:
        total += sum_metadata(child, 0)
    print "{} = {}".format(tree, total)
    return total


def generate_helper(node_list):
    new_node = Node(nb_nodes=node_list[0], nb_meta=node_list[1])
    node_list = node_list[2:]
    if new_node.nb_nodes == 0:
        new_node.metadata = node_list[:new_node.nb_meta]
        return new_node, node_list[new_node.nb_meta:]
    for child in range(new_node.nb_nodes):
        new_child, node_list = generate_helper(node_list)
        new_node.nodes.append(new_child)
    new_node.metadata = node_list[:new_node.nb_meta]

    return new_node, node_list[new_node.nb_meta:]
    

if __name__ == '__main__':
    tree = generate_tree()
    print sum_metadata(tree, 0)
