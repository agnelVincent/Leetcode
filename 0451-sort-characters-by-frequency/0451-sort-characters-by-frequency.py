class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        freq = sorted(freq.items(), key = lambda i : -i[1])

        res = ''
        for i in freq:
            res += i[0] * i[1]
        
        return res