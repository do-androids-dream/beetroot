"""
Task 2

Writing tests for context manager

Take your implementation of the context manager class from Task 1 and write tests for it. Try to cover as many use cases
as you can, positive ones when a file exists and everything works as designed.
And also, write tests when your class raises errors or you have errors in the runtime context suite.
"""
import logging
import os
import unittest
from unittest.mock import patch

from hw21_task1 import CustomOpen


class CustomOpenTest(unittest.TestCase):
    test_msg = "test message"
    test_fp = "test.txt"
    log = False
    log_fp = "customopen_log.txt"

    def setUp(self):
        with open(self.test_fp, "w") as file:
            file.write(self.test_msg)

    def test_customopen_positive__log(self):
        self.log = True

        with CustomOpen(self.test_fp, mode="r", log=self.log) as test_file:
            self.result = test_file.read()

        self.assertEqual(self.result, self.test_msg)

        log_res = os.path.exists(self.log_fp)
        self.assertTrue(log_res)

    def test_customopen_positive__nolog(self):
        with CustomOpen(self.test_fp, mode="r") as test_file:
            self.result = test_file.read()

        self.assertEqual(self.result, self.test_msg)
        self.assertRaises(FileNotFoundError, open, self.log_fp)

    def test_customopen_negative__wrong_mode_value(self):
        with CustomOpen(self.test_fp, mode="test") as file:
            result = file

        self.assertEqual(result, None)

    def test_customopen_negative__wrong_mode_type(self):
        with CustomOpen(self.test_fp, mode=123) as file:
            result = file

        self.assertEqual(result, None)

    def tearDown(self):
        os.remove(self.test_fp)

        if self.log:
            logging.shutdown()
            os.remove("customopen_log.txt")


class CustomOpenNegative(unittest.TestCase):
    test_msg = "test message"
    test_fp = "test.txt"
    log = False
    log_fp = "customopen_log.txt"

    def test_customopen_negative__nofile(self):
        with CustomOpen(self.test_fp) as file:
            result = file

        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
