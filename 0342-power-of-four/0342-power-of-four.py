class Solution:
    def isPowerOfFour(self, n: int , x = 0) -> bool:
        if x**4 > n:
            return False
        if n == 4**x:
            return True
        return self.isPowerOfFour(n , x+1)
        