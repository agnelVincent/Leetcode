class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        i = 0
        x = 0
        while i < len(s):
            # print(i,spaces[x],x,res)
            if x < len(spaces) and i == spaces[x]:
                res += ' '
                x += 1
            res += s[i]
            i += 1

        return res