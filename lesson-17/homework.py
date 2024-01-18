"""
Task 1

Method overriding.

Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make their
own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.
"""
print("\n---Task 1---\n")


class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")


def animal_talk(some_animal):
    some_animal.talk()


a_1 = Dog()
a_2 = Cat()

animals = [a_1, a_2]
for animal in animals:
    animal_talk(animal)

"""
Task 2

Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books
"""
print("\n---Task 2---\n")


class Library:
    def __init__(self, name: str, books: list["Book"] = None, authors: list["Author"] = None):
        if not books:
            books = []
        if not authors:
            authors = set()
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author: "Author"):
        """returns an instance of Book class and adds the book to the books list for the current library"""

        book = author.write_book(name=name, year=year)
        if book:
            self.add_book(book)

    def add_book(self, book: "Book"):
        """adds the book to the books list for the current library"""

        for ex_book in self.books:
            if book.name == ex_book.name:
                if book.author == ex_book.author:
                    if book.year == ex_book.year:
                        return
        self.books.append(book)
        self.authors.add(book.author)

    def group_by_author(self, author: "Author") -> list["Book"]:
        """returns a list of all books grouped by the specified author"""

        grouped_by_author = []
        if author in self.authors:
            for book in self.books:
                if book.author is author:
                    grouped_by_author.append(book)
            return grouped_by_author
        print(f"Author {author.name} is not available in this library")

    def group_by_year(self, year: int) -> list["Book"]:
        """returns a list of all the books grouped by the specified year"""

        grouped_by_year = []
        for ex_book in self.books:
            if ex_book.year == year:
                grouped_by_year.append(ex_book)
        return grouped_by_year

    def __repr__(self):
        return f"Library object - name: {self.name} - books number: {len(self.books)}"

    def __str__(self):
        return f"Library '{self.name}' with {len(self.books)} books"


class Book:
    books_counter = 0

    def __init__(self, name: str, year: int, author: "Author"):
        Book.books_counter += 1
        self.count = Book.books_counter
        self.name = name
        self.year = year
        self.author = author

        author.books.append(self)

    def show_book_counter(self):
        """returns book count number out of all books counter"""

        return f"{self.count} out of {self.books_counter}"

    def __repr__(self):
        return f"Book object {self.count} out of {self.books_counter} total exists - name: {self.name}"

    def __str__(self):
        return f"Book {self.name}"


class Author:
    def __init__(self, name: str, country: str, birthday: str, books: list["Book"] = None):
        if not books:
            books = []
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def write_book(self, name: str, year: int):
        """create a book instance"""

        if not self.book_exists(book_name=name, book_year=year):
            book = Book(name, year, self)
            if book:
                return book

    def book_exists(self, book_name, book_year) -> bool:
        """checks if book was already written"""

        for ex_book in self.books:
            if ex_book.name == book_name:
                if ex_book.year == book_year:
                    print("such book already exists")
                    return True
        return False

    def __repr__(self):
        return f"Author object - name: {self.name} - books written: {len(self.books)}"

    def __str__(self):
        return f"Author {self.name}"

##############################################################################


library = Library("Korolenko State Scientific Library")
author_1 = Author("John Ronald Reuel Tolkien", "United Kingdom", "January 3, 1892")
author_2 = Author("Howard Phillips Lovecraft", "United States", "August 20, 1890")

print(library, author_1, author_2, sep="\n")

book_1 = author_1.write_book("The Hobbit", 1937)
book_2 = author_1.write_book("The Lord of the Rings", 1954)
author_1.write_book("The Silmarillion", 1977)

author_2.write_book("The Call of Cthulhu", 1928)
author_2.write_book("At the Mountains of Madness", 1937)  # in reality 1936

library.new_book("The Call of Cthulhu", 1928, author_2)  # creating a book which already exists

books = author_1.books + author_2.books
for book in books:
    library.add_book(book)

print("",
    library,
    f"grouped by {author_1} - {library.group_by_author(author_1)}",
    f"grouped by year 1937 - {library.group_by_year(1937)}",
    author_1,
    author_2,
    author_2.books,
    author_2.books[1].show_book_counter(),
    book_1,
    sep="\n***\n"
)

"""
Task 3

Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з 
належною перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction
"""
print("\n---Task 3 ---\n")


class FractionError(Exception):
    def __init__(self, msg: str):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return f"Fraction ERROR occurred -> {self.msg}"


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator <= 0:
            raise FractionError("denominator couldn't be zero")
        if numerator > denominator:
            raise FractionError("numerator should be less than denominator")
        if numerator % denominator == 0:
            fraction = self.resolve_fraction(numerator, denominator)
            self.numerator = fraction[0]
            self.denominator = fraction[1]
        else:
            self.numerator = numerator
            self.denominator = denominator

    def __add__(self, other: "Fraction"):
        if self.denominator != other.denominator:
            k_1 = self.denominator
            k_2 = other.denominator
        else:
            k_1 = k_2 = 1

        res_numerator = self.numerator * k_2 + other.numerator * k_1
        res_denominator = self.denominator * k_2

        if res_numerator % res_denominator:
            fraction = self.resolve_fraction(res_numerator, res_denominator)
            return Fraction(fraction[0], fraction[1])
        return res_numerator // res_denominator

    def __sub__(self, other: "Fraction"):
        if self.denominator != other.denominator:
            k_1 = self.denominator
            k_2 = other.denominator
        else:
            k_1 = k_2 = 1

        res_numerator = self.numerator * k_2 - other.numerator * k_1
        res_denominator = self.denominator * k_2

        if res_numerator:
            fraction = self.resolve_fraction(res_numerator, res_denominator)
            return Fraction(fraction[0], fraction[1])
        return 0

    def __mul__(self, other: "Fraction"):
        res_numerator = self.numerator * other.numerator
        res_denominator = self.denominator * other.denominator

        if res_numerator:
            fraction = self.resolve_fraction(res_numerator, res_denominator)
            return Fraction(fraction[0], fraction[1])
        return 0

    def __truediv__(self, other: "Fraction"):
        res_numerator = self.numerator * other.denominator
        res_denominator = self.denominator * other.numerator

        if res_numerator:
            fraction = self.resolve_fraction(res_numerator, res_denominator)
            if isinstance(fraction, tuple):
                if len(fraction) == 2:
                    return Fraction(fraction[0], fraction[1])
                else:
                    return fraction[0], Fraction(fraction[1], fraction[2])
            else:
                return fraction
        return 0

    def __eq__(self, other: "Fraction"):
        if self.numerator == other.numerator:
            if self.denominator == other.denominator:
                return True
        return False

    @staticmethod
    def resolve_fraction(numerator: int, denominator: int):
        if numerator < denominator:
            for i in range(abs(numerator), 1, -1):
                if numerator % i == 0 and denominator % i == 0:
                    numerator //= i
                    denominator //= i
                    break
        elif numerator % denominator == 0:
            return numerator // denominator
        else:
            integer = numerator // denominator
            numerator -= integer * denominator
            return integer, numerator, denominator
        return numerator, denominator

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y)
    print(x + y == Fraction(3, 4))

#############################################################
print("\n*******\n")
try:
    Fraction(2, 0)
except FractionError as e:
    print(e)

try:
    a = Fraction(5, 3)
except FractionError as e:
    print(e)

a = Fraction(1, 2)
b = Fraction(2, 4)
c = Fraction(2, 7)

print(a == b)

print(a * b)
print(a / b)
print(a / c)
