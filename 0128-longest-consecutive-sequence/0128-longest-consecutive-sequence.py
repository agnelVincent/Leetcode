class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <1:
            return 0
        x = list(dict.fromkeys(nums))
        x.sort()
        if len(x) < 3:
            if len(x) == 1:
                return 1
            c = 0
            for i in range(len(x)-1):
                if x[i]+1 == x[i+1]:
                    c += 1
            return c+1

        c = 1
        d = []
        flag = True
        for i in range(len(x)-1):
            if x[i] + 1 == x[i+1]:
                c += 1
                flag = True
            else:
                d.append(c)
                c = 1
                flag = False
        if flag:
            d.append(c)

        if len(d) > 0:
            return max(d)
        else:
            return len(x)


                
        