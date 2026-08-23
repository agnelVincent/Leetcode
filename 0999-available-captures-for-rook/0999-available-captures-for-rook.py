class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        res = 0
        check = None
        i = 0
        while i < len(board):
            found = False
            j = 0
            while j < len(board[i]):
                if board[i][j] == 'R':
                    check = [i,j]
                    found = True
                    break
                j += 1
            if found:
                break
            i += 1
        
        left = check[0]
        right = check[0]
        up = check[1] 
        down = check[1]
        
        while left >= 0:
            if board[check[0]][left] == 'B':
                break
            if board[check[0]][left] == 'p':
                res += 1
                break
            left -= 1

        while right < 8:
            if board[check[0]][right] == 'B':
                break
            if board[check[0]][right] == 'p':
                res += 1
                break
            right += 1

        while up >= 0:
            if board[up][check[1]] == 'B':
                break
            if board[up][check[1]] == 'p':
                res += 1
                break
            up -= 1 

        while down < 8:
            if board[down][check[1]] == 'B':
                break
            if board[down][check[1]] == 'p':
                res += 1
                break
            down += 1    

        return res        

