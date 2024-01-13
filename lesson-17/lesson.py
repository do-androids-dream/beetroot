class A:
    def __init__(self):
        self.a = 1


a = A()

print(getattr(a, "b", "***"))
print(hasattr(a, "b"))
setattr(a, "d", 123)
