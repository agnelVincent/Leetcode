class Solution:
    def replaceDigits(self, s: str) -> str:
        i = 0
        res = list(s)

        while i < len(res):
            if res[i].isdigit():
                res[i] = chr(ord(res[i-1]) + int(res[i]))
            i += 1
        
        return ''.join(res)