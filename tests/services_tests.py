import unittest
from testworck import services


class TestGetRandomString(unittest.TestCase):
    TEST_LENGTH = 9

    def test_is_alfa(self):
        self.assertEqual(services.get_random_string(self.TEST_LENGTH).isalpha(), True)

    def test_length(self):
        self.assertEqual(len(services.get_random_string(self.TEST_LENGTH)), self.TEST_LENGTH)

    def test_is_digit(self):
        self.assertEqual(services.get_random_string(self.TEST_LENGTH).isdigit(), False)

    def test_isascii(self):
        self.assertEqual(services.get_random_string(self.TEST_LENGTH).isascii(), True)
