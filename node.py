
class Node:

    def __init__(self, value=None):
        self.value = value
        self.nodes_in = set()
        self.nodes_out = set()
        self.id = None

    def __repr__(self):
        s = f'Node(id={self.id}'
        if self.value is not None:
            s += f', value={self.value}'
        if len(self.nodes_in):
            s += f', nodes_in={self.nodes_in}'
        if len(self.nodes_out):
            s += f', nodes_out={self.nodes_out}'
        s += ')'
        return s

    def set_id(self, index: int):
        self.id = index

    def get_id(self):
        return self.id

    def link_to(self, other):
        """self will point to other"""
        self.nodes_out.add(other.id)
        other.nodes_in.add(self.id)

    def co_link(self, other):
        """link both nodes to each other"""
        self.link_to(other)
        other.link_to(self)

    def set(self, value):
        """set node value"""
        self.value = value

    def get(self):
        """get node value"""
        return self.value

    def in_degree(self):
        """number of nodes that point to self"""
        return len(self.nodes_in)

    def out_degree(self):
        """number of nodes that self points to"""
        return len(self.nodes_out)
