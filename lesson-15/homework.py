"""
Task 1

A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as
attributes. Make another method called talk() which makes prints a greeting from the person containing, for example like this: "Hello, my name is Carl Johnson and I’m 26 years old".
"""


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def call(self):
        fullname = self.firstname + " " + self.lastname
        print(f"Hello, my name is {fullname} and I’m {self.age} years old")


pers1 = Person("John", "Snow", 23)
pers2 = Person("Sansa", "Stark", 20)

pers1.call()
pers2.call()

"""
Task 2

Doggy age

Create a class Dog with class attribute 'age_factor' equals to 7. Make __init__() which takes values for a dog’s age. 
Then create a method `human_age` which returns the dog’s age in human equivalent.
"""


class Dog:
    age_factor = 7

    def __init__(self, dogage):
        self.age = dogage

    def human_age(self):
        return self.age * Dog.age_factor


rex = Dog(5)
print(rex.human_age())

"""
Task 3

TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
 

The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.
"""


CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels: list):
        self.channels = channels
        self.curr_ch = 0

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, ch: int):
        return self.channels[ch-1]

    def next_channel(self):
        if self.curr_ch < len(self.channels) - 1:
            self.curr_ch += 1
        return self.channels[self.curr_ch]

    def previous_channel(self):
        if self.curr_ch > 0:
            self.curr_ch -= 1
        return self.channels[self.curr_ch]

    def current_channel(self):
        return self.channels[self.curr_ch]

    def exists(self, ch):
        if isinstance(ch, int):
            if ch <= len(self.channels):
                resp = "Yes"
            else:
                resp = "No"
        else:
            if ch in self.channels:
                resp = "Yes"
            else:
                resp = "No"
        return resp


controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"

assert controller.last_channel() == "TV1000"

assert controller.turn_channel(1) == "BBC"

assert controller.next_channel() == "Discovery"

assert controller.previous_channel() == "BBC"

assert controller.current_channel() == "BBC"

assert controller.exists(4) == "No"

assert controller.exists("BBC") == "Yes"

####

assert controller.next_channel() == "Discovery"
assert controller.next_channel() == "TV1000"
assert controller.next_channel() == "TV1000"
