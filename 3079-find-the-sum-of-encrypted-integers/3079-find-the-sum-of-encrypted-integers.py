class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        x = []
        for i in nums:
            c = str(i)
            x.append(int(max(c) * len(c)))
        return sum(x)