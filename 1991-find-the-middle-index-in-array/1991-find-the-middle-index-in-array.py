class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            print(nums[:i],nums[i:])
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
            i += 1
        return -1