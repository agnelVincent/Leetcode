class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        x = dict(sorted({i:nums.count(i) for i in set(nums)}.items() , key = lambda i : i[1] , reverse = True)[:k])
        return [i for i in x]

        