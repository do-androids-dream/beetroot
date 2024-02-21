from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

        # prev added
        self.prev = None

    # changed to property
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: Any):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next: Optional["Node"]):
        self._next = new_next

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, new_prev: Optional["Node"]):
        self._prev = new_prev


"""
Task 1

Extend UnsortedList

Implement append, index, pop, insert methods for UnsortedList. Also implement a slice method, 
which will take two parameters 'start' and 'stop', and return a copy of the list starting at the position and going up to but not including the stop position.
"""


class UnsortedList:

    def __init__(self):
        self._head = None

        # tail added
        self._tail = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        new_node = Node(item)
        new_node.next = self._head

        if self._head is not None:
            new_node.next.prev = new_node

        self._head = new_node
        if self._tail is None:
            self._tail = new_node

    # append implemented
    def append(self, item: Any):
        new_node = Node(item)
        new_node.prev = self._tail
        if new_node.prev is not None:
            new_node.prev.next = new_node

        self._tail = new_node
        if self._head is None:
            self._head = new_node

    # pop added
    def pop(self) -> Any:
        poped_item = None
        if self._tail is not None:
            poped_item = self._tail.data
            self._tail = self._tail.prev
            self._tail.next = None
        return poped_item

    # insert implemented
    def insert(self, item: Any, insert_index: int):
        new_node = Node(item)
        current = self._head
        prev = None
        index = 0
        while current is not None and index < insert_index:
            index += 1
            prev = current
            current = current.next

        if prev is not None:
            prev.next = new_node
        new_node.next = current

        if index == 0:
            self._head = new_node
        if current is None:
            self._tail = new_node

    # index implemented with optional start-index
    def index(self, item: Any, start: int = 0) -> int:
        current = self._head
        index = 0
        while current is not None:
            if current.data == item and index >= start:
                return index
            index += 1
            current = current.next

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next

        #  added logic for append as it use tail
        if current.next is None:
            self._tail = previous

    # implemented slice
    def slice(self, start: int, stop: int) -> "UnsortedList":
        current = self._head
        index = 0
        new_list = UnsortedList()

        while current is not None and index < stop:
            if index >= start:
                new_list.append(current.data)
            index += 1
            current = current.next

        return new_list

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.data} > "
            current = current.next
        return representation


if __name__ == "__main__":
    my_list = UnsortedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    print(my_list)
    my_list.remove(31)
    print(my_list)
    print("*" * 10)
    print(my_list.size())
    print(my_list.search(93))
    print("*" * 10)
    my_list.append(11)
    print(my_list)
    my_list.remove(17)
    print(my_list)
    my_list.add(1)
    print(my_list)
    my_list.append(102)
    print(my_list)
    my_list.append(1)
    my_list.append(2)
    print(my_list)
    my_list.add(0)
    print(my_list)
    my_list.remove(0)
    print(my_list)
    my_list.add(22)
    print(my_list)
    print(my_list.index(100))
    print(my_list.index(2))
    print(my_list.index(10))
    my_list.append(100)
    print(my_list)
    print(my_list.index(100, 3))

    my_empty_list = UnsortedList()
    print(my_empty_list.index(2, 2))
    print(my_list.pop())
    print(my_list)
    print(my_empty_list.pop())
    print(my_empty_list)
    my_list.append(120)
    print(my_list)
    my_list.insert(2, 2)
    print(my_list)
    my_list.insert(0, 0)
    print(my_list)
    my_list.insert(123, 15)
    print(my_list)

    my_empty_list.insert(2, 15)
    my_empty_list.insert(3, 15)
    my_empty_list.insert(1, 0)
    print(my_empty_list)

    print(my_list.slice(0, 4))

"""
Task 2

Implement a stack using a singly linked list.
"""


class CustomStack:
    def __init__(self):
        self._head = None

    def push(self, item: Any):
        new_node = Node(item)
        current = self._head
        prev = None

        if self._head is None:
            self._head = new_node
        else:
            while current is not None:
                prev = current
                current = current.next
            prev.next = new_node

    def pop(self) -> Optional[int]:
        current = self._head
        temp = None
        prev = None

        if self._head is None:
            return None

        while current is not None:
            temp = current
            current = current.next

        current = self._head

        if current is temp:
            self._head = None

        while current is not temp:
            prev = current
            current = current.next
        if prev is not None:
            prev.next = None

        return current.data

    def __repr__(self) -> str:
        current = self._head
        result = f"CustomStack: "

        while current is not None:
            result += f"{current.data} > "
            current = current.next

        return result


stack = CustomStack()
print(stack)
stack.push(0)
print(stack)
stack.push(1)
print(stack)
stack.push(2)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
stack.push(22)
stack.push(23)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

"""
Task 3

Implement a queue using a singly linked list.
"""


class CustomQueue(UnsortedList):

    def get_item(self) -> Optional[Any]:
        item = None
        if self._head is not None:
            item = self._head.data
            self._head = self._head.next

        return item

    def pop(self):
        pass

    def add(self, item):
        pass

    def __repr__(self):
        representation = "<Queue: "
        current = self._head
        while current is not None:
            representation += f"{current.data} < "
            current = current.next
        return representation


q = CustomQueue()
q.append(1)
print(q)
q.append(2)
print(q)
q.append(3)
print(q)
print(q.get_item())
print(q)
print(q.get_item())
print(q)
print(q.get_item())
print(q)
print(q.get_item())
print(q)
