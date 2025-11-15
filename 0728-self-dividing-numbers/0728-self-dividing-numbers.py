class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(left,right+1):
            x = str(i)
            flag = True
            for num in x:
                if int(num) == 0 or i % int(num) !=0:
                    flag = False
                    break
            if flag:
                res.append(i)
        
        return res