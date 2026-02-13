class Solution:
    def isFascinating(self, n: int) -> bool:
        res = ''
        for i in range(1,4):
            res += str(i*n)

        return len([i for i in res if i != '0']) == 9