class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        i = 1
        res = 0
        nums.sort()

        while i < len(nums) - 1 and len(nums) > 2:
            allow = 0
            if nums[i] > nums[i-1]:
                allow += 1
            else:
                for j in range(i):
                    if nums[j] < nums[i]:
                        allow += 1
                        break
            if nums[i] < nums[i+1]:
                allow += 1
            else:
                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i]:
                        allow += 1
                        break
                if not allow:
                    return res
            print(allow)
            if allow == 2:
                res += 1
                nums.pop(i)
                i -= 1
            
            i += 1

        return res