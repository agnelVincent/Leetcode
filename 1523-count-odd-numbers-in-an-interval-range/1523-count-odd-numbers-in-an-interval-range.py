class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high - 1 if high % 2 == 0 else high) - (low + 1 if low % 2 == 0 else low)) // 2 + 1