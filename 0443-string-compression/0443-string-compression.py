class Solution:
    def compress(self, chars: List[str]) -> int:

        i = 0
        while i < len(chars):
            x = i
            while x < len(chars) and chars[i] == chars[x]:
                x += 1
            if x - i > 1:
                temp = str(x - i)
                chars[i + 1 : x] = [i for i in temp]
                i += 1 + len(temp)
            else:
                i += 1
        
        return len(chars)