import unittest
from homework import Email


class EmailValidationTest(unittest.TestCase):
    valid_emails = (
        '"John..Doe"@example.com',
        'John.Doe@com.ua',
        'John.Doe.12346789.123456789.123456789@com.ua',
        'John#.Doe@com.ua',
        'abc-d@mail.com',
        'JohnDoe@mail.com',
    )

    invalid_emails = (
        'John..Doe@example.com',
        '-johndoe@gmail.com',
        'John--Doe@gmail.com',
        'John..Doe@com.ua',
        'abc-d-@mail.com',
        'John.Doe.12346789.123456789.123456789.123456789.123456789.123456789@com.ua',
        ' @com',
        'John.Doe.12346789.123456789.123456789.@com.ua',
        '.John.Doe.12346789.123456789.123456789@com.ua',
        'John.Doe@com.u',
        'John.Doe@com.',
        'John@Doe@com.ua',
        '"John@Doe"@com.ua',
        'John..Doe@com.ua.',
    )

    def test_valid_emails_validation(self):
        for email in self.valid_emails:
            result = Email.validate(email)
            self.assertTrue(result, msg=email)

    def test_invalid_emails_validation(self):
        for email in self.invalid_emails:
            result = Email.validate(email)
            self.assertFalse(result, msg=email)


if __name__ == "__main__":
    unittest.main()
