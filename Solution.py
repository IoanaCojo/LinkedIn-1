from collections import deque
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = deque()
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in ['}', ')', ']'] and (not stack or matching[char] != stack.pop()):
                return False

        return len(stack) == 0

    # ''' if ()
    #      stack.append(
    #  openP = ''
    #
    #  key = matching.keys()
    #  val = matching.values()
    #
    #  # if len(s) <= 1 or s[0] in val:
    #  #     return False
    #
    #  for par in s:
    #      if par in key:
    #          openP += par
    #      elif par in val:
    #          if len(openP) == 0 or matching[openP[len(openP) - 1]] != par:
    #              return False
    #          else:
    #              openP = openP[:-1]
    #  if len(openP) != 0:
    #      return False
    #  print('True')
    #  return True'''

    def removeElement1(self, nums: List[int], val: int) -> int:
        if ((len(nums) == 1 and nums[0] == val) or len(nums) == 0):
            return 0
        first = 0
        last = len(nums) - 1
        while first < last:
            if nums[first] == val:
                # dummy2 = last
                while nums[last] == val:
                    last -= 1
                dummy = nums[first]
                nums[first] = nums[last]
                nums[last] = dummy

            first += 1
        print(nums)
        return nums

    def removeElement2(self, nums: List[int], val: int) -> int:
        if ((len(nums) == 1 and nums[0] == val) or len(nums) == 0):
            return 0
        elif len(nums) == 1 and nums[0] != val:
            return 1

        first = 0
        last = len(nums) - 1
        while first < last:
            if nums[first] == val:
                # dummy2 = last
                while nums[last] == val:
                    last -= 1
                    if last == 0:
                        return 0
                dummy = nums[first]
                nums[first] = nums[last]
                nums[last] = dummy
            first += 1
        print(first)

        return nums

# return [x for x in nums if x != val];

# value : int = 1;
# for element in nums :
#     if element == val:
#         nums.remove(val)
#
# print(nums)
# return nums

#
# nums = sorted(nums)
# minval = 0
# maxval = len(nums) - 1
# midval = 0
#
# while minval <= maxval:
#     midval = (maxval + minval) // 2
#     if nums[midval] < val:
#         minval = midval + 1
#     elif nums[midval] > val:
#         maxval = midval - 1
#     else:
#         #while minval+1 <= maxval:
#         if nums[minval] == val:
#             nums.remove(val)
#                 #maxval -= 1
#             #minval += 1
# if nums[len(nums)-1] == val:
#     nums.pop()
#
# print (nums)

# while nums.remove(val) != 0:
#   print('true')
# le = len(nums)
# for index in range(le):
# if nums[le] == val:
# pass
# print(nums)

sol = Solution()
sol.removeElement2([3,3],2)
# [0,1,4,0,3]
