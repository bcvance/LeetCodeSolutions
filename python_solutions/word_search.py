class Solution:
    def exist(self, board, word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        seen = set()

        def backtrack(r=0,c=0,i=0):
            if i >= len(word):
                return True
            if (r<0 or c<0 or r>=ROWS or c>=COLS or board[r][c] != word[i] or (r,c) in seen):
                return False
            seen.add((r,c))
            res = (backtrack(r-1, c, i+1) or backtrack(r, c-1, i+1) or backtrack(r, c+1, i+1) or backtrack(r+1, c, i+1))
            seen.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0):
                    return True
        return False
        
            
                    