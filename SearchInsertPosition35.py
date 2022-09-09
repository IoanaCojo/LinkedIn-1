'''
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''
from typing import List


class SearchInsertPosition35:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) - 1
        mid = 0
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2 and target > nums[0]:
            return 1
        elif len(nums) <= 2 and target < nums[0]:
            return 0
        elif len(nums) == 2 and target > nums[1]:
            return 2

        while min <= max:
            mid = (max + min) // 2
            if mid == min and min == max:
                if target < nums[mid] and mid > 0:
                    return mid - 1
                elif target < nums[mid] and mid == 0:
                    return 0
                elif target > nums[mid]:
                    return mid + 1

            elif nums[mid] < target:
                min = mid + 1
            elif nums[mid] > target:
                max = mid - 1
            elif nums[mid] == target:
                return mid

search = SearchInsertPosition35()
print(search.searchInsert([1,3], 2))
