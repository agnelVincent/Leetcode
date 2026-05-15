class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        import math
        return math.floor(s.count(letter)/len(s) * 100)