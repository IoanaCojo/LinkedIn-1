from unittest import TestCase

from Solution import Solution


class TestSolution(TestCase):
    def test_is_valid(self):
        solution = Solution()

        self.assertTrue(solution.isValid(""));
        self.assertFalse(solution.isValid(")"));

        self.assertTrue(solution.isValid("{[()]}"));
        self.assertTrue(solution.isValid("[()[]]"));

        # self.assertFalse(solution.isValid("}asdf(asdfs)"));
        # self.assertTrue(solution.isValid(""));
        # self.assertFalse(solution.isValid("}"));



    def test_remove_element1(self):
        solution = Solution()
        self.assertListEqual([0, 1, 4, 0, 3, 2, 2, 2], solution.removeElement1([0, 1, 2, 2, 3, 0, 4, 2], 2) );
        self.assertListEqual([], solution.removeElement2([0], 0) );
        self.assertListEqual([], solution.removeElement2([], 2) );

    def test_remove_element2(self):
        solution = Solution()
        self.assertListEqual([0, 1, 4, 0, 3, 2, 2, 2], solution.removeElement2([0, 1, 2, 2, 3, 0, 4, 2], 2) );
        self.assertListEqual([3,3], solution.removeElement2([3,3], 5) );
        #self.assertListEqual([], solution.removeElement1([], 2) );

