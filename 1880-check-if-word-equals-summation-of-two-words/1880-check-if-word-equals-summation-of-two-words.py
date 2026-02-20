class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f1 = [str(ord(i)-ord('a')) for i in firstWord]
        f2 = [str(ord(i)-ord('a')) for i in secondWord]
        t = [str(ord(i)-ord('a')) for i in targetWord]
        return True if int(''.join(f1)) + int(''.join(f2)) == int(''.join(t)) else False
