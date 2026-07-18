class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
        peaks = n // 2
        return s + peaks * m - (peaks - 1)