class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        n = 1
        # arr2 = list(dict.fromkeys(arr))
        while i < k:
            if arr:
                if n == arr[0]:
                    arr.pop(0)
                else:
                    i += 1
            else:
                i += 1
            n += 1
        
        return n