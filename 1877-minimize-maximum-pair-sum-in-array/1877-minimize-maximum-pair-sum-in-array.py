class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[:len(nums)//2] + nums[-1:-1-len(nums)//2:-1]
        return max([nums[i] + nums[i+len(nums)//2] for i in range(len(nums)//2)])