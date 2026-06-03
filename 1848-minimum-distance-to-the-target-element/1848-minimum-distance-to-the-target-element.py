class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        i = 0
        res = []
        while i < len(nums):
            if nums[i] == target:
                res.append(abs(i - start))
            i += 1
        return min(res)