from typing import Any, Optional, Generator, Iterable


class LinkedQueueError(Exception):
    pass


class EndOfLinkedQueueError(LinkedQueueError):
    pass


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional[Node] = None


class LinkedQueue:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

    def iterate(self) -> Iterable[Any]:
        current = self.head

        while current is not None:
            yield current.value
            current = current.next

    def push(self, item: Any):
        node = Node(item)

        if self.head is None:
            self.head = node

        if self.tail is not None:
            self.tail.next = node

        self.tail = node

        self.size += 1

    def pop(self) -> Any:
        if self.head is None:
            raise EndOfLinkedQueueError()

        node = self.head
        if node.next is not None:
            self.head = node.next
        else:
            self.head = None
            self.tail = None

        self.size -= 1

        return node.value

    def get_size(self):
        return self.size


if __name__ == '__main__':
    q = LinkedQueue()
    q.push('Gandalf')
    q.push('Frodo')
    q.push('Aragorn')
    q.push('Gimli')
    for user in q.iterate():
        print(f'-> {user}', end='')

    print()
    print(q.pop())
    print(q.pop())
    print(q.get_size())
    print(q.pop())
    print(q.pop())
    # print(q.pop())
    print(q.get_size())

middle = len(lst) // 2