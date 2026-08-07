class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        a = 1
        while a <= len(arr):
            i = 0
            while i < len(arr) and i + a <= len(arr):
                res += sum(arr[i:i+a])
                i += 1
            a += 2
        return res