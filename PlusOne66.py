'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [7,9,9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
'''
from typing import List


class PlusOne66:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = -1
        new_nums=[]
        if digits[index] != 9:
            digits[index] += 1
            return digits

        while digits[index] == 9:
            digits[index] = 0
            if index == - len(digits):
                new_nums.append(1)
                new_nums += digits
                return new_nums
            elif index != - len(digits) and digits[index-1]!=9:
                digits[index-1] = digits[index-1] + 1
                return digits
            index -= 1
        return digits

add = PlusOne66()
add.plusOne([8,9,9])