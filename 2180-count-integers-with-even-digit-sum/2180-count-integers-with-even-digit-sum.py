class Solution:
    def countEven(self, num: int) -> int:

        c = 0

        for i in range(1,num+1):
            if i<10:
                if i%2 == 0:
                    c+=1
            elif i>=10:
                b = str(i)
                sum = 0
                for j in range(len(b)):
                    sum += int(b[j])
                if sum%2 == 0 and sum != 0 and sum <= num:
                    c += 1
        return c
        