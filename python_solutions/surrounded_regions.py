class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()

        def dfs_mark(r, c):
            if (r<0 or c<0 or
            r >= ROWS or c >= COLS or 
            (r, c) in visited or 
            board[r][c] == "X"):
                return
            visited.add((r, c))
            dfs_mark(r-1, c)
            dfs_mark(r+1, c)
            dfs_mark(r, c-1)
            dfs_mark(r, c+1)

        def dfs_flip(r, c):
            if (r<0 or c<0 or
            r >= ROWS or c >= COLS or 
            (r, c) in visited or 
            board[r][c] == "X"):
                return
            visited.add((r, c))
            board[r][c] = "X"
            dfs_flip(r-1, c)
            dfs_flip(r+1, c)
            dfs_flip(r, c-1)
            dfs_flip(r, c+1)

        for r in range(ROWS):
            dfs_mark(r, 0)
            dfs_mark(r, COLS-1)

        for c in range(COLS):
            dfs_mark(0, c)
            dfs_mark(ROWS-1, c)

        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                dfs_flip(r, c)

        return board

        
