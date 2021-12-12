import numpy as np
from node import Node


def where(v: list):
    """returns dict that indicates the position of each (unique) value in the list"""
    return {j: i for i, j in enumerate(v)}


class Graph:
    def __init__(self):
        self.nodes = dict()
        self.node_count = 0

    def __getitem__(self, item) -> Node:
        return self.nodes[item]

    def __setitem__(self, key: int, value):
        self.nodes[key] = value

    def __iter__(self):
        return iter(self.nodes)

    def __contains__(self, item):
        return item in self.nodes

    def __repr__(self):
        s = ("\n" + " " * 6).join([str(self[i]) for i in self])
        return f'Graph({s})'

    def n(self):
        """returns numbers of nodes"""
        return len(self.nodes)

    def set(self, index, value):
        """set node value"""
        self[index].set(value)

    def get(self, index):
        """set node value"""
        return self[index].get()

    def in_degree(self, index):
        """number of nodes that point to node of given index"""
        return self[index].in_degree()

    def out_degree(self, index):
        """number of nodes that the node of given index points to"""
        return self[index].out_degree()

    def _get_new_index(self):
        """return node counter, increase node count by one"""
        self.node_count += 1
        return self.node_count - 1

    def add(self, node: Node) -> int:
        """adds node to self, returns index of that node"""
        index = self._get_new_index()
        self[index] = node
        node.set_id(index)
        return index

    def add_nodes(self, *nodes):
        for node in nodes:
            self.add(node)

    def remove(self, index):
        """delete node"""
        for i in self[index].nodes_in:
            self[i].nodes_out.remove(index)
        self.nodes.pop(index)

    def adj_list(self):
        """adjacency list"""
        return [list(self[i].nodes_out) for i in self]

    def adj(self):
        """adjacency matrix (rows indicate the nodes that each node points to)"""
        mat = np.zeros((self.n(), self.n()), dtype=int)
        indices = list(iter(self))
        w = where(indices)
        for i in self:
            for j in self[i].nodes_out:
                mat[w[i], w[j]] = 1
        return mat

    def assert_contains(self, *indices):
        """make sure self contains indices, else raise appropriate error"""
        for i in indices:
            if i not in self:
                raise ValueError(f'node {i} not in graph')

    def link_to(self, index_1, index_2):
        """link first node to the second one"""
        self.assert_contains(index_1, index_2)
        self[index_1].link_to(self[index_2])

    def co_link(self, index_1, index_2):
        """co-link first and second node"""
        self.assert_contains(index_1, index_2)
        self[index_1].co_link(self[index_2])

    def distance(self, index_1, index_2):
        """minimum number od steps required to connect two nodes"""
        if index_1 == index_2:
            return 0
        explored = {index_1}
        frontier = {index_1}
        i = 0
        while True:
            new = set()
            for j in frontier:
                for k in self[j].nodes_out:
                    if k not in explored:
                        if k == index_2:
                            return i
                        new.add(k)
            if not len(new):
                return
            frontier = new
            explored = set.union(explored, new)
            i += 1
