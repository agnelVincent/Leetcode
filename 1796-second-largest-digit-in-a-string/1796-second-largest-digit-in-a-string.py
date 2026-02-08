class Solution:
    def secondHighest(self, s: str) -> int:
        res = set()
        for i in s:
            if i.isdigit():
                res.add(int(i))
        
        if not set or not len(res) > 1:
            return -1

        return sorted(list(res))[-2]
