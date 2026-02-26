class Solution:
    def removeDigit(self, number: str, digit: str) -> str:        
        res = []
        i = 0

        while i < len(number):
            if number[i] == digit:
                res.append(int(number[:i] + number[i+1:]))
            i += 1
        
        return str(max(res))