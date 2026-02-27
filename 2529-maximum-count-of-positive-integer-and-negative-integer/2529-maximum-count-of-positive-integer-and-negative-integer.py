class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return len(max([i for i in nums if i > 0],[i for i in nums if i < 0], key = lambda i : len(i)))