class Solution:
    def reverseDegree(self, s: str) -> int:
        
        res = 0
        alp = {chr(i) : abs(i-123) for i in range(122,96,-1)}


        i = 0
        while i < len(s):
            res += ((i+1)*alp[s[i]])
            i += 1

        return res