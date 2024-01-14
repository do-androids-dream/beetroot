"""
Task 1

School

Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute, while salary should only be available to the teacher.
"""
print("---task 1---")

class Person:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age
        self.cur_location = "Home"

    def walk_to(self, to_location):
        self.cur_location = to_location.lower()
        print(f"{self.name} came to {to_location}\n" if to_location == 'school' else f"{self.name} came {to_location}\n")

    def introduce_to(self, to_whom):
        print(f"Dear {to_whom.profession}, I'm {self.name} and I don't have any profession :(")


class Student(Person):
    profession = "student"

    def __init__(self, *args):
        super().__init__(args[0], args[1])
        self.skills = set()

    def study(self, skill):
        if self.cur_location == "school":
            print(f"{self.name} study {skill} at {self.cur_location}\n")
            self.skills.add(skill)
        else:
            print(f"Sorry, {self.name} is at {self.cur_location}\n")

    def introduce_to(self, to_whom):
        print(f"Dear {to_whom.profession}, I'm {self.name} a {self.profession}")
        print(f"I've got knowledge in {' ,'.join(self.skills)}\n" if self.skills else f"I've got no knowledge :(\n")


class Teacher(Person):
    profession = "teacher"

    def __init__(self, *args):
        super().__init__(args[0], args[1])
        self.subject = args[2]

    def teach(self, whom):
        print(f"{self.name} start teaching {self.subject}\n")
        for pers in whom:
            pers.study(self.subject)

    def introduce_to(self, to_whom):
        print(f"Dear {to_whom.profession}s, I'm {self.name} the {self.profession} of {self.subject}\n")


def create_person(cls, *args):
    return cls(*args)


ST_CAPS = [
    (Student, "John", 16),
    (Student, "Mirinda", 17),
]

TCH_CAPS = [
    (Teacher, "Bob", 45, "Math"),
    (Teacher, "Shawn", 65, "Literature"),
]


def school_life():
    print("\n---8am---\n")
    students = {}
    count = 0
    for student in ST_CAPS:
        count += 1
        students[f"p{count}"] = create_person(*student)

    teachers = {}
    count = 0
    for teacher in TCH_CAPS:
        count += 1
        teachers[f"p{count}"] = create_person(*teacher)

    for teacher in teachers:
        teachers[teacher].walk_to("school")
    for student in students:
        students[student].walk_to("school")
        students[student].introduce_to(Teacher)

    teachers["p1"].introduce_to(Student)
    teachers["p1"].teach(students.values())

    print("---the lesson is over---\n")

    students["p2"].walk_to("home")

    print("---the next lesson---\n")

    teachers["p2"].introduce_to(Student)
    teachers["p2"].teach(students.values())

    print("---the lesson is over---\n")

################################################

    for student in students:
        students[student].introduce_to(Student)

################################################


school_life()

"""
Task 2

Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
"""
print("---task 2---")

class Mathematician:
    @staticmethod
    def square_nums(lst):
        return [el**2 for el in lst]

    @staticmethod
    def remove_positives(lst):
        return [el for el in lst if el < 0]

    @staticmethod
    def filter_leaps(lst):
        return [year for year in lst if year % 4 == 0]  # simplified


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

print(m.remove_positives([26, -11, -8, 13, -90]))
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


"""
Task 3

Product Store

Write a class Product that has three attributes:

type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
"""
print("---task 3---")


class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.price_premium = 1.3
        self.income = 0

    def add(self, product, amount):
        self.products[product.name] = {
            "type": product.type,
            "name": product.name,
            "price": product.price,
            "discount": 0,
            "store price": round(product.price * self.price_premium),
            "amount": amount,
        }

    def set_discount(self, identifier, percent, identifier_type="name"):
        if percent > 1:
            percent = percent / 100
        if identifier_type == "name":
            self.products[identifier]["discount"] = percent
            self.products[identifier]["store price"] *= 1 - percent
        else:
            for product in self.products.values():
                if product[identifier_type] == identifier:
                    product["discount"] = percent
                    product["store price"] *= 1 - percent

    def sell_product(self, product_name, amount):
        if product_name in self.products:
            if self.products[product_name]["amount"] >= amount:
                self.products[product_name]["amount"] -= amount
                self.income += amount * self.products[product_name]["store price"]
                print(f"Sell of {product_name} in amount {amount} proceed successfully, available amount in store: {self.products[product_name]["amount"]}")
            else:
                print(f"Sorry, available amount of {product_name} is {self.products[product_name]["amount"]}")

    def get_income(self):
        print("Store's income:", self.income, "USD")
        return self.income

    def get_all_products(self):
        print("Available in the store:")
        for product in self.products.keys():
            print("-", product)

    def get_product_info(self, product_name):
        if product_name in self.products:
            product = self.products[product_name]
            print(f"Product info: \n-product: {product['name']}\n-amount: {product["amount"]}")
            return (product["name"], product["amount"])



p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.get_income()

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)

########################################
print("----------EXTRA TESTS-----------")
s.get_income()

print(s.products)

s.set_discount("Sport", 30, "type")
s.set_discount("Ramen", 10)

print("----after discount applied\n", s.products, sep="")
print("\n---trying to buy more than available")
s.sell_product("Ramen", 300)
print(s.products)
s.get_income()

print("\n---trying to buy available amount")
s.sell_product("Ramen", 250)
s.get_income()
s.get_all_products()

print(s.get_product_info(product_name="Ramen"))

"""
Task 4

Custom exception

Create your custom exception named 'CustomException', you can inherit from base Exception class, 
but extend its functionality to log every error message to a file named 'logs.txt'. Tips: Use __init__ method to extend functionality for saving messages to file
"""
print("\n---Task 4---\n")

from datetime import datetime


class CustomException(Exception):
    def __init__(self, msg):
        self.msg = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-Custom ERROR occurred, I don't know what to do... " + msg + "\n"
        with open("logs.txt", "a") as file:
            file.write(self.msg)


try:
    raise CustomException("Ooops, keep calm!")
except CustomException:
    pass

try:
    raise CustomException("Oh, no... not again!")
except CustomException as e:
    print(e)


