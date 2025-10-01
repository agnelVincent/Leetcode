class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_len = 0
        ind = {}
        i = 0
        while i < len(s):
            if s[i] in ind and ind[s[i]] >= start:
                start = ind[s[i]] + 1
            ind[s[i]] = i

            if i - start + 1 > max_len:
                max_len = i  - start + 1
            
            i+=1
        
        return max_len
