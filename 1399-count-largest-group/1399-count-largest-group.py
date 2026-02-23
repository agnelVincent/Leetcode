class Solution:
    def countLargestGroup(self, n: int) -> int:
        check = [list(str(i)) for i in range(1,n+1)]

        i = 0
        res_dict = {}

        while i < len(check):
            temp = [int(num) for num in check[i]]
            if sum(temp) not in res_dict:
                res_dict[sum(temp)] = []
            res_dict[sum(temp)].append(int(''.join(check[i])))
            i += 1
        
        return len([res_dict[i] for i in res_dict if len(res_dict[i]) == len(max(res_dict.values(),key = lambda i : len(i)))])
