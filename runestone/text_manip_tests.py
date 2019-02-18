import unittest
from text_manipulation import replace

class TextManipulationTests(unittest.TestCase):
    def test_returns_string(self):
        self.assertIsNotNone(replace("blah blah blah", "b", "c"))

    def test_returns_single_character_change(self):
        self.assertEqual(replace("blah blah blah", "b", "c"), "clah clah clah")

    def test_returns_multi_character_change(self):
        self.assertEqual(replace("blah blah blah", "bl", "ch"), "chah chah chah")