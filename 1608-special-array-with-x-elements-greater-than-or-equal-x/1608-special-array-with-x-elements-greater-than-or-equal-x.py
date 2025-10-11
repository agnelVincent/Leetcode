class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            x = 0
            for j in nums:
                if j >= i:
                    x += 1
            if i == x:
                return i
        return -1
        
        
        