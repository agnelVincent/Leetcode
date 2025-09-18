class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        x = text.split()
        res = 0
        for i in x:
            flag = 1
            for j in i:
                if j in brokenLetters:
                    flag = 0
                    break
            if flag:
                res += 1
        return res