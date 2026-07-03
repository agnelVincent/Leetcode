class Solution:
    def modifyString(self, s: str) -> str:
        ch = 97
        res = list(s)

        i = 0
        while i < len(res):
            if res[i] == '?':
                visited = set()
                if i - 1 >= 0:
                    visited.add(ord(res[i-1]))
                if i + 1 < len(res):
                    visited.add(ord(res[i+1]))
                for x in range(97,124):
                    if x not in visited:
                        res[i] = chr(x)
                        break
            i += 1
        
        return res