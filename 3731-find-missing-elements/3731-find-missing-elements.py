class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start = min(nums)
        end = max(nums)
        return [i for i in range(start,end) if i not in nums]