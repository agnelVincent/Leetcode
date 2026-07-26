class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        i = 0
        prev = None
        freq = 1
        while i < len(s):
            if s[i] == prev:
                freq += 1
            else:
                prev = s[i]
                freq = 1
            if freq == 3:
                i += 1
                freq -= 1
                continue
            res += s[i]
            i += 1
        return res