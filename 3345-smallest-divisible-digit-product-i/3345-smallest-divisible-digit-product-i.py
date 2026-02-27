class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while True:
            check = [int(i) for i in str(n)]
            import math
            if math.prod(check) % t == 0:
                return n
            n += 1
