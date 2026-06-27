class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        w1 = list(s1)
        w2 = list(s2)

        i = 0
        while i < 2:
            if w1[i] != w2[i]:
                w1[i+2], w1[i] = w1[i], w1[i+2]
            if w1 == w2:
                return True
            i += 1
            
        return False