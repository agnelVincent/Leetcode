class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        srev = ''.join(reversed(list(s)))
        i = 0
        while i < len(srev)-1:
            if srev[i:i+2] in s:
                return True
            i += 1
        return False