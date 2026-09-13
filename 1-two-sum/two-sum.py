class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in nums:
                for j in range(i + 1, len(nums)):
                    if nums[j] == difference:
                        return [i, j]