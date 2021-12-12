from node import Node
from graph import Graph


class Assert:
    count = 0

    def __init__(self, x, message=None):
        Assert.count += 1
        if message:
            assert x, message
        else:
            assert x
        print(f'> Test {self.count} passed!')


def test_node():
    node_a = Node(value='A')
    node_a.set_id(0)
    node_b = Node(value='B')
    node_b.set_id(1)
    node_c = Node(value='C')
    node_c.set_id(2)
    node_a.co_link(node_b)
    node_a.link_to(node_c)

    print(node_a)
    print(node_b)
    print(node_c)

    Assert(node_a.nodes_in == {1})
    Assert(node_b.nodes_in == {0})
    Assert(node_c.nodes_in == {0})
    Assert(node_a.nodes_out == {1, 2})
    Assert(node_b.nodes_out == {0})
    Assert(node_c.nodes_out == set())


def test_graph_building():
    graph = Graph()
    nodes = [Node(value) for value in ('A', 'B', 'C')]

    for node in nodes:
        i = graph.add(node)
        Assert(type(i) is int)

    Assert(graph.n() == 3)

    graph.co_link(0, 1)
    graph.link_to(2, 0)

    print(graph)

    Assert(graph[0].nodes_in == {1, 2})
    Assert(graph.in_degree(0) == 2)
    Assert(graph[1].nodes_out == {0})
    Assert(graph.out_degree(1) == 1)
    Assert(graph[2].nodes_out == {0})

    graph.remove(0)
    Assert(graph[1].nodes_out == set())
    Assert(graph[2].nodes_out == set())


def test_graph_adj():
    graph = Graph()
    nodes = [Node(value) for value in ('A', 'B', 'C')]

    for node in nodes:
        i = graph.add(node)
        Assert(type(i) is int)

    graph.co_link(0, 1)
    graph.link_to(0, 2)

    print(graph)
    print(graph.adj())
    Assert(graph.adj()[0, 2] == 1)

    print(graph.adj_list())
    Assert(graph.adj_list() == [[1, 2], [0], []])


def test_graph_distance():
    n = 5
    graph = Graph()
    nodes = [Node(value=i) for i in range(n+1)]
    graph.add_nodes(*nodes)

    graph.link_to(0, 0)
    graph.link_to(0, 1)
    graph.co_link(0, 2)

    print(graph)
    Assert(graph.distance(0, n) is None)

    graph.link_to(2, n)

    print(graph)
    Assert(graph.distance(0, 0) == 0)
    Assert(graph.distance(0, 1) == 1)
    Assert(graph.distance(0, n) == 2)


if __name__ == "__main__":
    test_node()
    test_graph_building()
    test_graph_adj()
    test_graph_distance()
