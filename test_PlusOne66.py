from unittest import TestCase
from PlusOne66 import PlusOne66

class TestPlusOne66(TestCase):
    def test_plus_one(self):
        test = PlusOne66()

        self.assertListEqual([1,2,4], test.plusOne([1,2,3]))
        self.assertListEqual([1, 3, 0], test.plusOne([1, 2, 9]))
        self.assertListEqual([1,0], test.plusOne([9]))
        self.assertListEqual([1,0,0], test.plusOne([9,9]))
