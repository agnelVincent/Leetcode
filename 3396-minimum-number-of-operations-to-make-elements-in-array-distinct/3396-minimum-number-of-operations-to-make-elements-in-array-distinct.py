class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i = 0
        c = 0
        while i < len(nums):
            if len(nums[i:]) == len(set(nums[i:])):
                return c
            i += 3
            c += 1
        
        return c