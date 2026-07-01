class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(min(nums))
        i = 0
        while i < len(nums):
            res = res.intersection(nums[i])
            i += 1
        return sorted(list(res))