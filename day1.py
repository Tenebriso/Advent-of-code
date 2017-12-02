class Node:
    def __init__(self, value):
        self._value = value
        self._is_first = False
        self._is_last = False

    def is_first(self):
        return self._is_first

    def is_last(self):
        return self._is_last

    def mark_first(self):
        self._is_first = True

    def mark_last(self):
        self._is_last = True

    def unmark_last(self):
        self._is_last = False

    def unmark_first(self):
        self._is_first = False

    def __str__(self):
        return str(self._value)

class CircularList:
    def __init__(self):
        self._data = []
        self._current = None

    def add_node(self, value):
        new_node = Node(value)
        if not self._data:
            new_node.mark_last()
            new_node.mark_first()
            self._current = 0
        else:
            new_node.mark_last()
            self._data[len(self._data) - 1].unmark_last()
        self._data.append(new_node)

    def value(self):
        return self._data[_current]

    def next(self):
        self._current += 1
        if self._current == len(self._data):
            self._current = 0
        return self._data[_current]

    def length(self):
        return len(self._data)

    def __str__(self):
        return " ".join([str(x) for x in self._data])

def reader(filename):
    with open(filename) as f:
        while True:
            c = f.read(1)
            if not c or c == '\n':
                return
            else:
                yield c

if __name__ == '__main__':
    r = reader('input_file')
    c = CircularList()
    first = r.next()
    current = first
    c.add_node(first)
    suma = 0
    while True:
        try:
            nxt = r.next()
            c.add_node(nxt)
        except StopIteration:
            if current == first:
                suma += int(current)
            break
        if nxt == current:
            suma += int(current)
        current = nxt
    print("Suma: {}".format(suma))
    print(c)
