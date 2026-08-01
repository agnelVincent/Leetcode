class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([x for i in matrix for x in i])[k-1]