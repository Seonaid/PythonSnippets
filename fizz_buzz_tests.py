import unittest
from fizz_buzz import fizz_buzz

class FizzBuzzTests(unittest.TestCase):
    def test_returns_something(self):
        self.assertIsNotNone(fizz_buzz())

    def test_3_fizz(self):
        self.assertEqual(fizz_buzz(3), {3: 'fizz'})

    def test_several_fizz_buzz(self):
        self.assertEqual(fizz_buzz(4, 6, 15, 3, 10), {6: 'fizz', 15: 'fizz_buzz', 3: 'fizz', 10: 'buzz'})

    # def test_rejects_list(self):
    #     self.assertRaises(TypeError, fizz_buzz, [4, 6, 15, 3, 10])

    def test_handles_list(self):
        self.assertEqual(fizz_buzz([4, 6, 15, 3, 10]), 'sent list')