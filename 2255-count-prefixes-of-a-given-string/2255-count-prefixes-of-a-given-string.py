class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        i = 0
        while i < len(words):
            if words[i] == s[:len(words[i])]:
                res += 1
            i += 1
        return res