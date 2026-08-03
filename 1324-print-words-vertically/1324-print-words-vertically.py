class Solution:
    def printVertically(self, s: str) -> List[str]:
        c = s.split()
        res = []
        i = 0
        while i < len(max(c, key = lambda i : len(i))):
            t = ''
            x = 0
            while x < len(c):
                t += c[x][i] if i < len(c[x]) else ' '
                x += 1
            i += 1
            res.append(t.rstrip())

        return res
        