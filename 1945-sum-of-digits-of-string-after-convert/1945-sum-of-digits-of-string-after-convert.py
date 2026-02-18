class Solution:
    def getLucky(self, s: str, k: int) -> int:
        checking = ""
        for i in s:
            checking += str(ord(i) - ord("a") + 1)

        def transform(n):
            checking = str(n)
            res = 0
            for i in checking:
                res += int(i)
            return res

        final = int(checking)
        for i in range(k):
            final = transform(final)

        return final
