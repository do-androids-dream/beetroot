
import time
from typing import Any


class Queue:
    def __init__(self):
        self._storage = []

    def pop(self) -> Any:
        return self._storage.pop(0)

    def append(self, val: Any) -> None:
        self._storage.append(val)

    def get_size(self) -> int:
        return len(self._storage)

    def __len__(self):
        return self.get_size()

    def __str__(self):
        return f"{self._storage}"

    def __bool__(self):
        return bool(self.get_size())


def process(item):
    time.sleep(0.5)
    print(f"{item} processed")


def handle_queue(queue: Queue):
    while queue:
        val = queue.pop()
        process(val)
        print(f"q: {queue}")


if __name__ == "__main__":
    started_at = time.time()

    vals = input(f"Users: ")
    q = Queue()
    for val in vals:
        q.append(val)
    print(f"q: {q}")

    handle_queue(q)

    print(f"q: {q}")

    print(f"Took {time.time() - started_at:.2f} seconds")
