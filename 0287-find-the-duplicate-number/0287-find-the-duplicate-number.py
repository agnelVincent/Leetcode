class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = set()
        for i in nums:
            if i not in freq:
                freq.add(i)
            else:
                return i