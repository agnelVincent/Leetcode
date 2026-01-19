class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = set()
        steps = 0
        while len(nums) and len(res) != k:
            if nums[len(nums)-1] <= k:
                res.add(nums.pop(-1))
            else:
                nums.pop(-1)
            steps += 1
        return steps