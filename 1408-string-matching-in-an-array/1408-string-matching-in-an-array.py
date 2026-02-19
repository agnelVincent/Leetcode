class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        checking = sorted(words, key = lambda i : len(i))
        
        res = []

        for i in range(len(checking)-1):
            for j in range(i+1,len(checking)):
                if checking[i] in checking[j]:
                    res.append(checking[i])
                    break
        
        return res