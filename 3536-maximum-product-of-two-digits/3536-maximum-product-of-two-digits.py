class Solution:
    def maxProduct(self, n: int) -> int:
        x = sorted(str(n))
        return int(x[-1]) * int(x[-2])
        
