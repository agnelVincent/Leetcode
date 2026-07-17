class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        res = '1'

        while i < n:
            temp_res = ''
            x = 0

            while x < len(res):
                check = res[x]
                t = x

                while t < len(res) and res[t] == check:
                    t += 1

                temp_res += str(t - x) + check
                x = t
                
            res = temp_res
            i += 1
        
        return res
