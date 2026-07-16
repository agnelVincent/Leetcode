class Solution:
    def reverse(self, x: int) -> int:
        
        check = str(x)[::-1]
        if check[-1] == '-':
            res = -int(check[:-1])
            if res > -2 ** 31 and res < 2 ** 31 - 1:
                return res
            else:
                return 0
        res = int(check)
        return res if res > -2 ** 31 and res < 2 ** 31 - 1 else 0