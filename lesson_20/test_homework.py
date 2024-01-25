import unittest

from unittest.mock import patch
from lesson_11.phonebook.modules.operations import validate_record, create_record


class PhoneBookRecordValidation(unittest.TestCase):

    @patch("lesson_11.phonebook.modules.operations.load_phonebook")
    def test_phone_number_value__correct(self, mock_load_phonebook):
        mock_load_phonebook.return_value = []
        field = "telephone number"
        value = "+380123456789"

        result = validate_record(field, value, "")
        self.assertTrue(result)

    @patch("lesson_11.phonebook.modules.operations.load_phonebook")
    def test_phonebook_number_value__incorrect(self, mock_load_phonebook):
        mock_load_phonebook.return_value = []
        field = "telephone number"
        value = "abcdefghijklm"

        result = validate_record(field, value, "")
        self.assertFalse(result)

    @patch("lesson_11.phonebook.modules.operations.load_phonebook")
    def test_phone_number_correct_value__existing_same_number(self, mock_load_phonebook):
        mock_load_phonebook.return_value = [{"telephone number": "+380123456789"},]
        field = "telephone number"
        value = "+380123456789"

        result = validate_record(field, value, "")
        self.assertFalse(result)

    @patch("lesson_11.phonebook.modules.operations.load_phonebook")
    def test_phone_number_correct_value__existing_different_number(self, mock_load_phonebook):
        mock_load_phonebook.return_value = [{"telephone number": "+389876543210"},]
        field = "telephone number"
        value = "+380123456789"

        result = validate_record(field, value, "")
        self.assertTrue(result)

    @patch("lesson_11.phonebook.modules.operations.load_phonebook")
    def test_phone_number_length__incorrect(self, mock_load_phonebook):
        mock_load_phonebook.return_value = []
        field = "telephone number"
        value = "+0123456"

        result = validate_record(field, value, "")
        self.assertFalse(result)

    @patch("lesson_11.phonebook.modules.operations.load_phonebook")
    def test_phone_number_value__empty(self, mock_load_phonebook):
        mock_load_phonebook.return_value = []
        field = "telephone number"
        value = ""

        result = validate_record(field, value, "")
        self.assertFalse(result)

    @patch("lesson_11.phonebook.modules.operations.load_phonebook")
    def test_name_value__correct(self, mock_load_phonebook):
        mock_load_phonebook.return_value = []
        field = "first name"
        value = "abcdefgh"

        result = validate_record(field, value, "")
        self.assertTrue(result)

    @patch("lesson_11.phonebook.modules.operations.load_phonebook")
    def test_name_value__incorrect(self, mock_load_phonebook):
        mock_load_phonebook.return_value = []
        field = "first name"
        value = "0123456"

        result = validate_record(field, value, "")
        self.assertFalse(result)

    @patch("lesson_11.phonebook.modules.operations.load_phonebook")
    def test_name_value__empty(self, mock_load_phonebook):
        mock_load_phonebook.return_value = []
        field = "first name"
        value = ""

        result = validate_record(field, value, "")
        self.assertFalse(result)

    @patch("lesson_11.phonebook.modules.operations.load_phonebook")
    def test_name_correct_value__existing_same_f_name(self, mock_load_phonebook):
        mock_load_phonebook.return_value = [{"first name": "first"}]
        field = "first name"
        value = "first"

        result = validate_record(field, value, "")
        self.assertTrue(result)

    @patch("lesson_11.phonebook.modules.operations.load_phonebook")
    def test_name_correct_value__existing_same_l_name(self, mock_load_phonebook):
        mock_load_phonebook.return_value = [{"last name": "last"}]
        field = "last name"
        value = "last"

        result = validate_record(field, value, "")
        self.assertTrue(result)


class PhoneBookRecordCreation(unittest.TestCase):

    @patch("lesson_11.phonebook.modules.operations.input")
    @patch("lesson_11.phonebook.modules.operations.save_new_record")
    @patch("lesson_11.phonebook.modules.operations.validate_record")
    def test_create_record__correct(self, mock_validate_record, mock_save_new_record, mock_input):
        mock_validate_record.return_value = True
        mock_save_new_record.return_value = None
        mock_input.return_value = "Test"

        expected = {
            "first name": "Test",
            "last name": "Test",
            "telephone number": "+Test",
            "city": "Test",
            "state": "Test"
        }
        result = create_record("file_p")
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
