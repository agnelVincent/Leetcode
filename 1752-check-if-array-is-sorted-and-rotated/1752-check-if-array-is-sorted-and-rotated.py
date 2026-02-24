class Solution:
    def check(self, nums: List[int]) -> bool:
        checking = sorted(nums)
        
        i = 0
        while i < len(checking):
            if checking == nums:
                return True
            checking.insert(0,checking.pop())
            i += 1

        return False