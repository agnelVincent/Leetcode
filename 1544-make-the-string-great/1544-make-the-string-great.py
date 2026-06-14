class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        letter = list(s)

        while i < len(letter) - 1:
            print(letter,i)
            if letter[i].lower() == letter[i+1].lower():
                if letter[i] != letter[i+1]:
                    letter.pop(i)
                    letter.pop(i)
                    i = 0
                    continue
            i += 1

        return ''.join(letter)