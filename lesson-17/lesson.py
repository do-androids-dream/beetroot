from abc import ABC, abstractmethod


class A:
    def __init__(self):
        self.a = 1


a = A()

print(getattr(a, "b", "***"))
print(hasattr(a, "b"))
setattr(a, "d", 123)


class Lesson(ABC):
    @abstractmethod
    def do_homework(self):
        pass


class Lesson11(Lesson):
    pass


l = Lesson11()


