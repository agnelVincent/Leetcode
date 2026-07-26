class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        res = sorted(nums)
        p = res[-1] * res[-2] * res[-3]
        n = res[0] * res[1] * res[-1]

        return max(p,n)