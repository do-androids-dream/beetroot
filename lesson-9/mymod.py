"""study module for lesson-9 Task-3"""

file_path = "file.txt"

with open(file_path) as some_file:
    file_content = some_file.read()
    print("Content of file: ", "----start----", file_content, "----end----", sep="\n")


def count_lines(name):
    file = open(name)
    lines = file.readlines()
    file.close()
    return len(lines)


def count_chars(name):
    file = open(name)
    content = file.read()
    words = len(content.split())
    chars = len(content)
    file.close()
    return words, chars


def test(name):
    for i in range(1, 3):
        lines = count_lines(name)
        chars = count_chars(name)
        print("\nTest", i)
        print(f"There is {lines} lines in the file")
        print(f"and {chars[0]} words and {chars[1]} characters")


if __name__ == "main":
    test(file_path)
