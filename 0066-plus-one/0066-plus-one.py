class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''
        for i in digits:
            a += str(i)
        b = int(a) + 1
        c = []
        for i in str(b):
            c.append(int(i))
        return c
        