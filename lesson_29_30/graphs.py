graph = {
    "A": [
        ["B", 3],
    ],
    "B": [
        ["C", 300],
        ["E", 7],
    ],
    "C": [
        ["D", 20],
    ],
    "D": [],
    "E": [
        ["F", 300],
    ],
    "F": []
}


def df_search(start, end, path=None):
    if path is None:
        path = [start]

    if start == end:
        return path

    for node, length in graph.get(start, []):
        if node not in path:
            new_path = find_path(node, end, path + [node])
            if new_path:
                return new_path

    return None


print(find_path("A", "F"))
print(find_path("A", "D"))
print(find_path("B", "F"))
print(find_path("F", "A"))
