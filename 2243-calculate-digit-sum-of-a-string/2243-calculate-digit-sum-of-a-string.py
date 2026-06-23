class Solution:
    def digitSum(self, s: str, k: int) -> str:
       
        check = s

        while len(check) > k:
            dig_split = [check[i:i+k] for i in range(0,len(check),k)]
            dig_sum = [str(sum(int(digit) for digit in num)) for num in dig_split]
            check = ''.join(dig_sum)

        return check
