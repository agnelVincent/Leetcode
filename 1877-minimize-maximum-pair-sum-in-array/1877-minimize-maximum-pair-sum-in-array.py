class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        x1 = nums[:len(nums)//2]
        x2 = nums[-1:-1-len(nums)//2:-1]
        return max([x1[i]+x2[i] for i in range(len(x1))])