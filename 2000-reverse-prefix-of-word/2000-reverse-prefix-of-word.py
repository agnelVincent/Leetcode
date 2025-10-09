class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for ind , val in enumerate(word):
            if val == ch:
                return ''.join(reversed(list(word[:ind+1]))) + word[ind+1:] 
        return word