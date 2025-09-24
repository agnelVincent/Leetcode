class Solution:
    def isPowerOfFour(self, n: int , x = 0) -> bool:
        if n == 4**x:
            return True
        if x**4 > n:
            return False
        return self.isPowerOfFour(n , x+1)
        