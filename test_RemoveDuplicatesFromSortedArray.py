from unittest import TestCase
from RemoveDuplicatesFromSortedArray import RemoveDeplicatesFromSortedArray


class TestRemoveDeplicatesFromSortedArray(TestCase):
    def test_remove_duplicates_is_valid(self):
        tests = RemoveDeplicatesFromSortedArray()
        self.assertListEqual(tests.removeDuplicates([]), [])
        self.assertListEqual(tests.removeDuplicates([1]), [1])
        self.assertListEqual(tests.removeDuplicates([1,2,2,5,3]),[1,2,3,5])