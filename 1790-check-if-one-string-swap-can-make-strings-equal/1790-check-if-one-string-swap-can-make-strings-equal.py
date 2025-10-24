class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        x = []
        y = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                x.append(s1[i])
                y.append(s2[i])
        return len(x) <= 2 and sorted(x) == sorted(y)
            
            