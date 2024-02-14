import time
from typing import Any


class Stack:
    def __init__(self):
        self._storage = []

    def pop(self) -> Any:
        return self._storage.pop()

    def append(self, val: Any):
        self._storage.append(val)

    def get_size(self) -> int:
        return len(self._storage)

    def __len__(self) -> int:
        return self.get_size()

    def __str__(self) -> str:
        return f"{self._storage}"

    def __bool__(self) -> bool:
        return bool(self.get_size())


def process(item):
    time.sleep(0.5)
    print(f"{item} processed")


def handle_stack(stack):
    while len(stack) > 0:
        val = stack.pop()
        process(val)
        print(f"q: {stack}")


if __name__ == "__main__":
    started_at = time.time()

    vals = input(f"Users: ")
    s = list(vals)
    print(f"q: {s}")

    handle_stack(s)

    print(f"q: {s}")

    print(f"Took {time.time() - started_at:.2f} seconds")