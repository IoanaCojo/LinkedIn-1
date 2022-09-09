from unittest import TestCase
from LengthOfLastWord58 import LengthOfLastWord58


class TestLengthOfLastWord58(TestCase):
    def test_length_of_last_word(self):
        test = LengthOfLastWord58()

        self.assertEqual(6,test.lengthOfLastWord('eu am banane'))
        self.assertEqual(0, test.lengthOfLastWord(''))