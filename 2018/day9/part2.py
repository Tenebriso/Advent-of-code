INPUT_FILE = 'input'
class Node:
    def __init__(self, value):
        self.value = value
        self.next= None
        self.back = None

class CircularLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.head.next = self.head
        self.head.back = self.head

    def remove(self, node_to_remove):
        while self.head.value != node_to_remove.value:
            self.head = self.head.next
        node_to_remove = self.head
        aux_next = node_to_remove.next
        aux_back = node_to_remove.back
        aux_back.next = aux_next
        aux_next.back = aux_back
        return aux_next
            

def read_marbles():
    with open(INPUT_FILE) as marble_file:
        line = marble_file.readline().strip().split()
    return int(line[0]), int(line[-2])


def compute_score(nb_players, nb_marbles):
    players_score = {x: 0 for x in range(nb_players)}
    circle = CircularLinkedList()
    current_marble = circle.head
    player = 0
    for marble in range(1, nb_marbles):
        player = (player + 1) % nb_players
        if marble % 23 == 0:
            for i in range(7):
                current_marble = current_marble.back
            players_score[player] += current_marble.value + marble
            current_marble = circle.remove(current_marble)
        else:
            m1 = current_marble.next
            m2 = current_marble.next.next
            new_node = Node(marble)
            m1.next = new_node
            m2.back = new_node
            new_node.next = m2
            new_node.back = m1
            current_marble = new_node
    return players_score


if __name__ == '__main__':
    nb_players, nb_marbles = read_marbles()
    print max(compute_score(nb_players, nb_marbles * 100).values())
