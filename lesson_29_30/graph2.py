from typing import Dict, Optional


class Node:
    def __init__(self, name: str):
        self.name = name
        self.edges = {}

    def add_edge(self, edges: Dict["Node", int]):
        self.edges.update(edges)
        for node, weight in edges.items():
            if self not in node.edges:
                node.add_edge({self: weight})

    def __repr__(self) -> str:
        return self.name


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node: Node, edges: Optional[Dict[Node, int]] = None):
        self.nodes.append(node)
        if edges:
            node.add_edge(edges)


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

graph = Graph()
graph.add_node(a)
graph.add_node(b, {a: 10})
graph.add_node(c, {b: 2, a: 5})
graph.add_node(d, {a: 1})
graph.add_node(e, {b: 15})
graph.add_node(f, {a: 5, b: 5, c: 5})

print(graph.nodes)
for node in graph.nodes:
    print(node, node.edges)
