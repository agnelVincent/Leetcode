class Solution:
    def generateTheString(self, n: int) -> str:
        res = ''
        if n%2 == 1:
            for i in range(n):
                res += 'a'
            return res
        else:
             for i in range(n):
                if (n - i) % 2 == 1:
                    for j in range(i,n):
                        res += 'b'
                    break
                res += 'a'
        return res

