class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while j < len(s):
                    if not s[j].isdigit():
                        break
                    j += 1
                if i != j:
                    if not int(s[i:j]) > prev:
                        return False
                    prev = int(s[i:j])
                    i = j - 1
                else:
                    if not int(s[i]) > prev:
                        return False
                    prev = int(s[i])
                    
            i += 1
        return True
