from unittest import TestCase
from SearchInsertPosition35 import SearchInsertPosition35


class TestSearchInsertPosition35(TestCase):
    def test_search_insert(self):
        test = SearchInsertPosition35()

        self.assertEqual(2,test.searchInsert([1,3,5,6],5))
        self.assertEqual(1,test.searchInsert([1,3,5,6],2))
        self.assertEqual(1,test.searchInsert([1,3], 2))
        self.assertEqual(0,test.searchInsert([1,3], 0))
        self.assertEqual(0,test.searchInsert([], 3))
        #



