class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            res = True
            j = 0
            check_arr = nums[:i] + nums[i+1:]
            while j < len(check_arr)-1:
                if not check_arr[j] < check_arr[j+1]:
                    res = False
                    break
                j += 1
            if res:
                return True
            i += 1
        return False 



