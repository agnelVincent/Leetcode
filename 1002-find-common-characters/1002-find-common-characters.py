class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        x = [list(i) for i in words]
        res = []
        chk = x[0]
        for i in chk:
            c = 1
            for val in range(1,len(x)):
                if i in x[val]:
                    c += 1
            if c == len(x):
                for val in range(1,len(x)):
                    x[val].remove(i)
                res.append(i)
        return res