class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for i in words:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        return [x[0] for x in sorted(freq.items(), key = lambda i : (-i[1],i[0]))[:k]]