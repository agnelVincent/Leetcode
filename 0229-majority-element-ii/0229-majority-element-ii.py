class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        i = 0
        while i < len(nums):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] += 1
            i += 1

        res = []
        i = 0
        
        for i in freq:
            if freq[i] > len(nums) / 3:
                res.append(i)
        
        return res