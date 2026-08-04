class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        i = 0
        res = []
        while i < len(words):
            if len(words[i]) != len(pattern):
                i += 1
                continue

            pat = {}
            visited = set()
            x = 0
            obeys = True
            while x < len(words[i]):
                if pattern[x] not in pat:
                    if words[i][x] in visited:
                        obeys = False
                        break
                    else:
                        pat[pattern[x]] = words[i][x]
                        visited.add(words[i][x])
                else:
                    if pat[pattern[x]] != words[i][x]:
                        obeys = False
                        break
                x += 1
            if obeys:
                res.append(words[i])
            i += 1

        return res