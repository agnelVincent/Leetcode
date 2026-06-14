class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()

        for ind,word in enumerate(words):
            if len(word) >= len(searchWord):
                if word[:len(searchWord)] == searchWord:
                    return ind + 1
        
        return -1