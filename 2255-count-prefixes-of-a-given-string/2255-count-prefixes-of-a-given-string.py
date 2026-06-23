class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return len([i for i in words if i == s[:len(i)]])