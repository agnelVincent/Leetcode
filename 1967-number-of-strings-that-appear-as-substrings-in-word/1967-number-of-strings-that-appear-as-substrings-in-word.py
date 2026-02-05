class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for i in patterns:
            for j in range(len(word)):
                if i == word[j:j+len(i)]:
                    res += 1
                    break
        
        return res