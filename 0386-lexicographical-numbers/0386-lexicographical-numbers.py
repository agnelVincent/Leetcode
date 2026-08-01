class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return [int(x) for x in sorted([str(i) for i in range(1,n+1)])]