class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = list(s)
        i = 0
        temp = len(res) - 1
        while i < temp:
            if res[i].isalpha():
                while temp >= 0:
                    if res[temp].isalpha():
                        res[i], res[temp] = res[temp], res[i]
                        temp -= 1
                        break
                    temp -= 1
            i += 1
                        
        return ''.join(res)