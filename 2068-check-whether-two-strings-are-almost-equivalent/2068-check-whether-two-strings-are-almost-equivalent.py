class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        checking = list(dict.fromkeys(list(word1) + list(word2)))

        i = 0

        while i < len(checking):
            if abs(word1.count(checking[i]) - word2.count(checking[i])) > 3:
                return False
            i += 1

        return True

