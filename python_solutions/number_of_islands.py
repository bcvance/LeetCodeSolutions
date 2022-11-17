class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            visited.add((r, c))
            q = deque()
            q.append((r, c))

            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

            while q:
                r, c = q.pop()
                visited.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nc >= 0 and
                    nr < rows and nc < cols and 
                    (nr, nc) not in visited and
                    grid[nr][nc] == "1"):
                        q.append((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if ((r, c) not in visited and 
                grid[r][c] == "1"):
                    bfs(r, c)
                    res += 1
        return res

