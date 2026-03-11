class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        ind = [float('inf')] * 2
        i = 0
        while i < len(capacity):
            if capacity[i] >= itemSize:
                if capacity[i] < ind[1]:
                    ind = [i,capacity[i]]
            i += 1

        return ind[0] if ind[0] != float('inf') else -1