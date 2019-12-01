from collections import defaultdict

INPUT_FILE = 'input'
NO_WORKERS = 5

graph = defaultdict(set)

def generate_graph():
    all_nodes = set()
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            line = line.strip().split()
            graph[line[-3]].add(line[1])
            all_nodes.add(line[-3])
            all_nodes.add(line[1])
    all_nodes = sorted(all_nodes)
    return all_nodes


def find_unsolved(solved, all_nodes, busy):
    for node in all_nodes:
        if node not in solved and node not in busy:
            unsolved = graph[node] - set(solved) 
            if not unsolved:
                return node
    return None


def parse_graph():
    all_nodes = generate_graph()
    solved = []
    busy = set()
    worker_node = {x : None for x in range(NO_WORKERS)}
    worker_status = defaultdict(int)
    count = 0
    while len(solved) != len(all_nodes):
        for worker in range(NO_WORKERS):
            if worker_status[worker] > 0:
                worker_status[worker] -= 1
            if worker_status[worker] == 0:
                if worker_node[worker]:
                    solved.append(worker_node[worker])
                new_work = find_unsolved(solved, all_nodes, busy)
                worker_node[worker] = new_work
                if new_work:
                    busy.add(new_work)
                    worker_status[worker] = 61 + ord(new_work) - ord('A')
        for worker in range(NO_WORKERS):
            if not worker_node[worker]:
                new_work = find_unsolved(solved,all_nodes, busy)
                worker_node[worker] = new_work
                if new_work:
                    busy.add(new_work)
                    worker_status[worker] = 61 + ord(new_work) - ord('A')
        if len(solved) == len(all_nodes):
            break
        count += 1

    return count

if __name__ == '__main__':
    print parse_graph()
