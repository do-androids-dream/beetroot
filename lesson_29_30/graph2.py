from typing import Dict, Optional
from collections import Counter


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

    def df_search(self, start: Node, visited: Optional[list[Node]] = None) -> Optional[list[Node]]:
        if visited is None:
            visited = []
        visited.append(start)

        for next_node in start.edges:
            if next_node not in visited:
                self.df_search(next_node, visited)

        return visited

    @staticmethod
    def bf_search(start: Node, visited: Optional[list[Node]] = None, queue: Optional[list[Node]] = None) -> Optional[list[Node]]:
        if visited is None:
            visited = []
        if queue is None:
            queue = []
        queue.insert(0, start)

        while queue:
            node = queue.pop()

            if node not in visited:
                visited.append(node)
                for next_node in node.edges:
                    queue.insert(0, next_node)

        return visited

    def find_strongly_connected_components(self, start: Node) -> Optional[list[Node]]:
        one_way = self.df_search(start)
        i = len(one_way)

        for start in one_way[::-1]:
            back_way = self.df_search(start)

            if Counter(back_way) == Counter(one_way[:i]):
                return one_way
            i -= 1
        return None

    @staticmethod
    def find_shortest_way(start: Node, end: Node, visited: Optional[list[Node]] = None, queue: Optional[list[Node]] = None):
        if visited is None:
            visited = []
        if queue is None:
            queue = []
        queue.insert(0, start)

        while queue:
            node = queue.pop()

            if end in visited:
                return visited

            if node not in visited:
                visited.append(node)
                for next_node in node.edges:
                    queue.insert(0, next_node)

        return visited


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")

graph = Graph()
graph.add_node(a)
graph.add_node(b, {a: 10})
graph.add_node(c, {b: 2, a: 5})
graph.add_node(d, {a: 1})
graph.add_node(e, {b: 15})
graph.add_node(f, {a: 5, b: 5, c: 5})
graph.add_node(g, {h: 2})
graph.add_node(h)

print(graph.nodes)
for node in graph.nodes:
    print(node, node.edges)
print("*" * 10)
print(graph.df_search(a))
print(graph.df_search(g))
print("*" * 10)
print(graph.bf_search(a))
print(graph.bf_search(g))
print("*" * 10)
print(graph.find_strongly_connected_components(a))
print(graph.find_strongly_connected_components(g))
print("*" * 10)
print(graph.find_shortest_way(a, e))
print(graph.find_shortest_way(a, c))
