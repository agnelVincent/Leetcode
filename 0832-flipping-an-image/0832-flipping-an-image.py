class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = [x[::-1] for x in image]
        return [[0 if i == 1 else 1 for i in x] for x in res]