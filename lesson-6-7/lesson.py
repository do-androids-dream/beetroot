from random import sample

some_string = input("enter your string: ")

for i in range(5):
    random_string = sample(some_string, len(some_string))
    print("".join(random_string))
print("original string: ", some_string)

