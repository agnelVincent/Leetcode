class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i % 10 == nums[i]:
                return i
            i += 1
        return -1