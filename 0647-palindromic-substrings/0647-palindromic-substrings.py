class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        i = 0
        c = {}
        while i < len(s):
            if s[i] not in c:
                c[s[i]] = [i]
            else:
                c[s[i]].append(i)
            i += 1

        for key in c:
            if len(c[key]) == 1:
                continue
            temp = c[key]
            for x in range(len(temp)-1):
                for y in range(x+1,len(temp)):
                    check = s[temp[x]:temp[y]+1]
                    if check == check[::-1]:
                        res += 1
                        
        return res