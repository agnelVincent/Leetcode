class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        couple = [[code[i] , businessLine[i] , isActive[i]] for i in range(len(code))]
        for i in range(len(couple)):
            flag = True
            for x in range(len(couple[i])):
                if x == 0:
                    if len(couple[i][x]) < 1:
                        flag = False
                        break
                    for ch in couple[i][x]:
                        if not ch.isdigit() and not ch.isalpha() and ch != '_':
                            flag = False
                            break
                if x == 1:
                    if couple[i][x] not in ["electronics", "grocery", "pharmacy", "restaurant"]:
                        flag = False
                        break
                if x == 2:
                    if couple[i][x] != True:
                        flag = False
                        break
            if flag:
                res.append([couple[i][0] , couple[i][1]])

        return [i[0] for i in sorted(res , key = lambda i : (i[1] , i[0]))]
