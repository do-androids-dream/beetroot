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
    def bf_search(
            start: Node,
            visited: Optional[list[Node]] = None,
            queue: Optional[list[Node]] = None
    ) -> Optional[list[Node]]:

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
    def find_shortest_way(
            start: Node,
            end: Node,
            visited: Optional[list[Node]] = None,
            queue: Optional[list[Node]] = None
    ) -> list[Node]:
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

    def find_all_paths(
            self,
            start: Node,
            end: Node,
            visited: Optional[list[Node]] = None
    ) -> list[Optional[Node]]:
        if visited is None:
            visited = []
        visited.append(start)

        if start == end:
            return [visited.copy()]

        all_paths = []

        for next_node in start.edges:
            if next_node not in visited:
                paths = self.find_all_paths(next_node, end, visited.copy())
                all_paths.append(paths)

        return self._return_all_paths(all_paths)

    def _return_all_paths(
            self,
            paths: list,
            all_paths: Optional[Node] = None
    ) -> list[Optional[list[Node]]]:

        if all_paths is None:
            all_paths = []

        for path in paths:
            if isinstance(path, list):
                if path and not isinstance(path[0], list):
                    all_paths.append(path)
                self._return_all_paths(path, all_paths)

        return all_paths

    def shortest_path(self, start: Node, end: Node) -> Optional[list[Node]]:
        paths = self.find_all_paths(start, end)
        if paths:
            return min(paths, key=len)

        return paths


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
print("*" * 10)
print(graph.find_all_paths(a, e))
print(graph.shortest_path(a, e))
print("*" * 10)
print(graph.find_all_paths(a, g))
print(graph.shortest_path(a, g))
print("*" * 10)
print(graph.find_all_paths(b, f))
print(graph.shortest_path(b, f))
