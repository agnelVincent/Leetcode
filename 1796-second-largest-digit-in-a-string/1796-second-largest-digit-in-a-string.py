class Solution:
    def secondHighest(self, s: str) -> int:
        res = set()
        for i in s:
            if i.isdigit():
                res.add(int(i))

        return sorted(list(res))[-2] if len(res) > 1 else -1
