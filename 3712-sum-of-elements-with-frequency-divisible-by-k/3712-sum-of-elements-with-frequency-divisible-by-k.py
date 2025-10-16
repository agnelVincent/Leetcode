class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        return sum([i for i in nums if nums.count(i) % k == 0])