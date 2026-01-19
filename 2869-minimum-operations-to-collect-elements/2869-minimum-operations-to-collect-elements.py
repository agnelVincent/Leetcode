class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = set()
        i = 0
        steps = 0
        while i < len(nums) and len(res) != k:
            if nums[len(nums)-1] <= k:
                res.add(nums.pop(-1))
            else:
                nums.pop(-1)
            steps += 1
        return steps