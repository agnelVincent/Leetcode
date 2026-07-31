class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows <= 1 or numRows >= len(s):
            return s

        if numRows == 2:
            return ''.join([s[i] for i in range(0,len(s),2)] + [s[i] for i in range(1,len(s),2)])

        temp = []
        i = 0
        while i < len(s):
            temp.append(s[i:i + numRows])
            i += numRows
            if i + 1 <= len(s):
                temp.append(' ' + s[i : i + numRows - 2] + ' ')
            i += numRows - 2

        if len(temp[-1]) != numRows:
            temp[-1] = temp[-1] + ' ' * (numRows - len(temp[-1])) 

        res = ''

        i = 0
        while i < numRows:
            x = 0
            while x < len(temp):
                if x % 2 == 0:
                    res += temp[x][i] if temp[x][i] != ' ' else ''
                else:
                    res += temp[x][-1-i] if temp[x][-1-i] != ' ' else ''
                x += 1
            i += 1

        return res.strip()
                    