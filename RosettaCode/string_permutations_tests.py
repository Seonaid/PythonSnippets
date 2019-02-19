import unittest
from string_permutations import permAlone

class StringPermutationTests(unittest.TestCase):
    def test_returns_number(self):
        self.assertIsInstance(permAlone("aab"), int)