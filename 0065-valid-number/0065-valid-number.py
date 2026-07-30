class Solution:
    def isNumber(self, s: str) -> bool:
        i = 0
        hasdot = False
        hasdigit = False
        hase = False
        while i < len(s):
            if s[i].isalpha() and s[i] != 'e' and s[i] != 'E':
                return False

            if s[i] == '-' or s[i] == '+':
                if i != 0:
                    if i - 1 >= 0 and not s[i - 1] == 'e' and not s[i - 1] == 'E':
                        return False
                    
                if hasdigit and not s[i - 1] == 'e' and not s[i - 1] == 'E':
                    return False
                if not i + 1 < len(s):
                    return False 
                if not s[i + 1].isdigit() and not s[i + 1] == '.':
                    return False
                if i - 1 >= 0 and i + 1 < len(s):
                    if s[i - 1].isdigit() and s[i + 1].isdigit():
                        return False
            
            if s[i] == '.':
                if hasdot or hase:
                    return False
                if i - 1 < 0 and len(s) == 1:
                    return False 
                if i + 1 < len(s):
                    if not s[i + 1].isdigit() and not s[i + 1] == 'e' and not s[i + 1] == 'E':
                        return False
                hasdot = True
            

            if s[i] == 'e' or s[i] == 'E':
                if not hasdigit or hase:
                    return False
                if i - 1 < 0:
                    return False
                if not i + 1 < len(s):
                    return False 
                if not s[i + 1] == '-' and not s[i + 1] == '+' and not s[i + 1].isdigit():
                    return False
                if not hase:
                    hase = True

            if s[i].isdigit() and not hasdigit:
                hasdigit = True

            i += 1
                

        return True if hasdigit else False