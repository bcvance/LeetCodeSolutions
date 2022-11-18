from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        max_area = [0]
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        def bfs(area=0):
            while q:
                row, col = q.pop()
                if (row, col) not in visited:
                    area += 1
                    visited.add((row, col))
                    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < ROWS and
                        0 <= nc < COLS and 
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1):
                            q.append((nr, nc))
            if area > max_area[0]:
                max_area[0] = area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    q.append((r, c))
                    bfs()
        return max_area[0]

                
                