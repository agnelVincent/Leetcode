class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat = {}
        pat2 = {}
        i = 0
        check = s.split()
        if len(check) != len(pattern):
            return False
            
        while i < len(check):
            if check[i] not in pat and pattern[i] not in pat2:
                pat2[pattern[i]] = check[i]
                pat[check[i]] = pattern[i]
            else:
                if check[i] in pat:
                    if pattern[i] not in pat2:
                        return False
                if pattern[i] in pat2:
                    if check[i] not in pat:
                        return False
                if pat[check[i]] != pattern[i] or pat2[pattern[i]] != check[i]:
                    return False

            i += 1

        return True