class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        freq = {}
        
        i = 0
        while i < len(paragraph):
            if paragraph[i].isalpha():
                x = i
                while x < len(paragraph) and paragraph[x].isalpha():
                    x += 1
                if paragraph[i:x].lower() not in freq:
                    if paragraph[i:x].lower() not in banned:
                        freq[paragraph[i:x].lower()] = 1
                else:
                    freq[paragraph[i:x].lower()] += 1
                i += x - i
            else:
                i += 1

        return sorted(freq.items(),key=lambda i : (i[1],i[0]))[-1][0]