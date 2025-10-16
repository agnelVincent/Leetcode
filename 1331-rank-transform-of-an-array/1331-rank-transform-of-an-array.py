class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        x = sorted([i for i in set(arr)])
        res = {i:ind+1 for ind,i in enumerate(x)}
        return [res[i] for i in arr]