class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        indexes = {}
        i = 0
        res = s[0]
        while i < len(s):
            if s[i] not in indexes:
                indexes[s[i]] = []
            indexes[s[i]].append(i)
            if len(indexes[s[i]]) > 1:
                check = indexes[s[i]]
                for x in check[:-1]:
                    temp = s[x:check[-1] + 1]
                    if temp == temp[::-1]:
                        if check[-1] - x + 1 > len(res):
                            res = s[x:check[-1] + 1]
            i += 1
        return res
        