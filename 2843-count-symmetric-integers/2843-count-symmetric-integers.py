class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        while low <= high:
            check = str(low)
            if len(check) % 2 == 1:
                low = 10 ** len(check)
                continue
            if sum([int(check[x]) for x in range(len(check)//2)]) == sum([int(check[x]) for x in range(len(check)//2,len(check))]):
                res += 1
            low += 1
        return res