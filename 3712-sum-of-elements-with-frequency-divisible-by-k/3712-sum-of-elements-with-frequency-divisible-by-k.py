class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        x = []
        for i in set(nums):
            if nums.count(i) % k == 0:
                x.append(i)
        return sum([i for i in nums if i in x])