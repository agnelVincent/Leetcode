class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        res = []
        i = 0
        while i < len(s):
            if s[i] == goal[0]:
                res.append(i)
            i += 1
        
        for i in res:
            if s[i:] + s[:i] == goal:
                return True

        return False