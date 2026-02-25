class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq = {}
        i = 0
        while i < len(words1):
            if words1[i] not in freq:
                freq[words1[i]] = 0
            freq[words1[i]] += 1
            i += 1
        freq = {i:freq[i] for i in freq if freq[i] == 1}
        
        i = 0

        while i < len(words2):
            if words2[i] in freq:
                freq[words2[i]] += 1
            i += 1

        return len([i for i in freq if freq[i] == 2])