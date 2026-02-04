class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = [[i,nums.count(i)] for i in list(dict.fromkeys(nums))]
        freq.sort(key = lambda i : (i[1],-i[0]) )
        return [j for i in [[i[0]] * i[1] for i in freq] for j in i]
