from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        max_min = 0
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh_oranges = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh_oranges > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == 1:
                             grid[nr][nc] = 2
                             fresh_oranges -= 1
                             q.append((nr, nc))
            max_min += 1
        if fresh_oranges > 0:
            return -1
        return max_min