class Solution:
    def totalMoney(self, n: int) -> int:
        val = 1
        inc = 0
        res = 0
        for i in range(n):
            if i > 0 and i % 7 == 0:
                inc += 1
                val = 1
            res += val + inc
            val += 1
        return res