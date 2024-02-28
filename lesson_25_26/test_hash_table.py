import unittest
from hw26 import HashTable


class HashTableTest(unittest.TestCase):
    capacity = 100

    def setUp(self):
        self.hashtable = HashTable(self.capacity)

    def test_create_hashtable_instance(self):
        self.assertIsNotNone(self.hashtable)

    def test_hashtable_capacity(self):
        self.assertEqual(len(self.hashtable), self.capacity)

    def test_hashtable__empty_values(self):
        expected = [None] * self.capacity

        self.assertEqual(self.hashtable.pairs, expected)

    def test_hashtable__key_value(self):
        keys = ["Hello", 123, True]
        values = ["world!", 321, False]

        for key, value in zip(keys, values):
            self.hashtable[key] = value

        for key, value in zip(keys, values):
            self.assertIn((key, value), self.hashtable.pairs)

    def test_hashtable__none_is_value(self):
        key = "key"
        value = None
        self.hashtable[key] = value

        self.assertIn((key, value), self.hashtable.pairs)

    def test_hashtable__get_value(self):
        keys = ["Hello", 123, True]
        values = ["world!", 321, False]

        for key, value in zip(keys, values):
            self.hashtable[key] = value

        for key, value in zip(keys, values):
            result = self.hashtable[key]
            self.assertEqual(result, value)

    def test_hashtable__get_value_no_key(self):
        keys = ["Hello", 123, True]
        values = ["world!", 321, False]
        missing_key = "missing key"

        for key, value in zip(keys, values):
            self.hashtable[key] = value

        self.assertRaises(KeyError, lambda: self.hashtable[missing_key])

    def test_hashtable__key_in(self):
        key = "key"
        value = "value"
        self.hashtable["key"] = value

        self.assertIn(key, self.hashtable)

    def test_hashtable__key_is_not_in(self):
        key = "key"

        self.assertNotIn(key, self.hashtable)

    def test_hashtable__get_existing_value(self):
        key = "key"
        value = "value"
        self.hashtable[key] = value
        result = self.hashtable.get(key)

        self.assertEqual(value, result)

    def test_hashtable__get_existing_value_when_default(self):
        key = "key"
        value = "value"
        default = "default"
        self.hashtable[key] = value
        result = self.hashtable.get(key, default)

        self.assertEqual(value, result)

    def test_hashtable__get_none_for_not_existing_value(self):
        key = "key"

        self.assertIsNone(self.hashtable.get(key))

    def test_hashtable__get_default_for_not_existing_value(self):
        key = "key"
        default = "default"
        result = self.hashtable.get(key, default)

        self.assertEqual(default, result)

    def test_hashtable__delete_value(self):
        key = "key"
        value = "value"
        self.hashtable[key] = value

        assert key in self.hashtable

        del self.hashtable[key]

        self.assertNotIn(key, self.hashtable)
        assert len(self.hashtable) == self.capacity

    def test_hashtable__delete_not_existing_value(self):
        key = "key"

        with self.assertRaises(KeyError):
            del self.hashtable[key]
