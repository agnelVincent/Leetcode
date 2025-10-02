class Solution:
    def checkRecord(self, s: str) -> bool:
        x = {'A' : 0}
        for i in range(len(s)):
            if s[i] == 'A':
                x['A'] += 1
                if x['A'] == 2:
                    return False
            if s[i] == 'L':

                if i <= len(s) - 3:
                    if s[i:i+3] == 'LLL':
                        return False
        return True
            