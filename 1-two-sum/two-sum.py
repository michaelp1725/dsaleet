class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # variables created
        allDiff = {}
        length = len(nums)
        
        # search through entire list until difference is found in hashmap
        for i in range(length):
            diff = target - nums[i]
            
            if diff in allDiff:
                return [allDiff[diff], i]
            
            allDiff[nums[i]] = i
        