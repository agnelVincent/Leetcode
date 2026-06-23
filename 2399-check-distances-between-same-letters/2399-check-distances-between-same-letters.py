class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:

        ind_check = list(dict.fromkeys(s))

        indices = {char : [i for i in range(len(s)) if char == s[i]] for char in ind_check}

        i = 0
        while i < 26:
            if chr(97+i) in indices:
                if indices[chr(97+i)][1] - indices[chr(97+i)][0] - 1 != distance[i]:
                    return False
            i += 1

        return True