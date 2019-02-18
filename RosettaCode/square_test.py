import unittest

from sum_of_squares import sum_of_squares

class SumOfSquaresTest(unittest.TestCase):
    # def test_function_exists(self):
    #     self.assertEqual(sum_of_squares([]), True)

    def test_single_list(self):
        self.assertEqual(sum_of_squares([4]), 16)

    def test_short_list(self):
        self.assertEqual(sum_of_squares([2, 3, 4]), 29)