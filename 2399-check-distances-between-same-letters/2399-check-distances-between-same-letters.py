class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:

        indices = {char : [i for i in range(len(s)) if char == s[i]] for char in s}

        i = 0
        while i < 26:
            char = chr(97+i)
            if char in indices:
                if indices[char][1] - indices[char][0] - 1 != distance[i]:
                    return False
            i += 1

        return True