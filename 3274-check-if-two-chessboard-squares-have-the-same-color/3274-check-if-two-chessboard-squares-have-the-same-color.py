class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        if ord(coordinate1[0]) % 2 == ord(coordinate2[0]) % 2:
            return int(coordinate1[1]) % 2 == int(coordinate2[1]) % 2
        else:
            return int(coordinate1[1]) % 2 != int(coordinate2[1]) % 2