class Graph():
    """ A graph. """

    def __init__(self, nodes, directed=False):
        """ Initializes a new graph with the given set of nodes. """
        self.nodes = nodes
        self.directed = directed

class Node():
    """ A node in a graph. Each node stores information about its (x, y) coordinates, as well as a set of its neighbours. """
    def __init__(self, x_pos, y_pos, neighbors):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.neighbors = neighbors