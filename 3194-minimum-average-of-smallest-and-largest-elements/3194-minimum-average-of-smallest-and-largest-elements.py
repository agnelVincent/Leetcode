class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avgs = []
        nums.sort()
        i = 0
        while i < len(nums):
            avgs.append((nums.pop(0) + nums.pop(-1))/2)
        
        return min(avgs)