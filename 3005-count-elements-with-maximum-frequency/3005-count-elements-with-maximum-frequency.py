class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        maximum = float('-inf')
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
            if freq[i] > maximum:
                maximum = freq[i]

        return sum([i for i in freq.values() if i == maximum])
        