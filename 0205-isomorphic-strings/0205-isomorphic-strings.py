class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def index_check(string):
            x = list(dict.fromkeys(string))
            return {char:[i for i,c in enumerate(string) if c == char] for char in x}
        ref1 = index_check(s)
        ref2 = index_check(t)
        return [ref1[i] for i in ref1] == [ref2[i] for i in ref2]