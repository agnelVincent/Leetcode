class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums) // 2:
            res += int(str(nums[i]) + str(nums[-1-i]))
            print(str(nums[i]) + str(nums[-1]))
            i += 1
            print(f'result is {res}')
        
        if len(nums) % 2 != 0:
            res += nums[i]

        return res