import unittest
from typing import Generator

from homework import with_index, in_range, Sentence


class HomeWork19TestTask1(unittest.TestCase):

    def test_with_index__return_type(self):
        value = [i for i in range(10)]
        result = with_index(value)
        self.assertIsInstance(result, Generator, f"returned {type(result)} instead of generator")

    def test_with_index__start_value(self):
        start = 10
        value = [i for i in range(10)]
        result = next(with_index(value, start))
        self.assertEqual(result[0], start, f"expected index {start}, got {result[0]}")

    def test_with_index__wrong_value(self):
        value = 20
        self.assertRaises(TypeError, next, with_index(value))


class HomeWork19TestTask2(unittest.TestCase):

    def test_in_range__negative_step(self):
        start = 0
        stop = -10
        step = -2
        expected = list(range(start, stop, step))
        result = list(in_range(start, stop, step))
        self.assertEqual(result, expected, msg=f"expected {expected}, got {result}")

    def test_in_range__zero_step(self):
        start = 0
        stop = 10
        step = 0
        self.assertRaises(ValueError, next, in_range(start, stop, step))


class HomeWork19TestTask2(unittest.TestCase):

    def test_sentence__for_in_iteration(self):
        value = "first second third"
        i = 0
        for result in Sentence(value):
            expected = value.split()[i]
            i += 1
            self.assertEqual(result, expected)

    def test_sentence__list_comprehension(self):
        value = "first second third"
        result = [word for word in Sentence(value)]
        expected = value.split()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
