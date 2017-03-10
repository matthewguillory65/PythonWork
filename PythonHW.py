class Node(object):
    def __init__(self, value, identifier):
        self._value = value
        self._identifier = identifier
    def print_info(self):
        print "value", self._value, "id", self._identifier


class Graphs(object):
    def __init__(self, x, y):
        self.nodes = {}
        for i in range(0, x):
            for j in range(0, y):
                n = Node([i, j], i * j)
                self.nodes[n] = i * j

def test_nodes():
    '''test the nodes'''
    graph = Graphs([3, 3, ])
    node = get_node(2, graph)
    node.print_info()
    neighbors = get_neighbors(node, graph)
    for nod in neighbors:
        nod.print_info()



if __name__ == '__main__':
    test_nodes()

