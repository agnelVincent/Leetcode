class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1

        x = dict(sorted(freq.items() , key = lambda i : i[1] , reverse = True))
        return [i for i in x.keys()][:k]