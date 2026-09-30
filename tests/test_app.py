import unittest
from src.app import add, multiply


class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
    def test_add_zero_and_negative_number(self):
        self.assertEqual(add(0, -4), -4)

if __name__ == "__main__":
    unittest.main()