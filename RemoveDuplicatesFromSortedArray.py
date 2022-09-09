class RemoveDeplicatesFromSortedArray:
    def removeDuplicates(self, nums):
        nums = sorted(nums)
        if len(nums) <= 1:
            return nums
        for index in range(1, len(nums) - 1):
            while index < len(nums) and nums[index] == nums[index - 1]:
                nums.remove(nums[index])

        return nums
        # if nums[len(nums) - 1] == nums[len(nums) - 2]:
        #     nums.pop()


    def removeDuplicatesSet(self, nums):
        print(set(nums))
        # for n in nums :
        #     a.add(n)
        # print(a)

    @staticmethod
    def revoveDups(nums):
        i = 0
        for e in range(1, len(nums) - 1):
            if nums[i] == nums[e]:
                while nums[e] == nums[e - 1]:
                    nums.remove(nums[e])
            else:
                i += 1
        print(nums)


test = RemoveDeplicatesFromSortedArray()
test.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
# test.revoveDups([1,2,2,2,2,3,4])
