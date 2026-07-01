class Solution:
    def checkString(self, s: str) -> bool:
        i = 0
        b = False
        while i < len(s):
            if s[i] == 'b':
                b = True
            if s[i] == 'a' and b:
                return False
            i += 1
        return True