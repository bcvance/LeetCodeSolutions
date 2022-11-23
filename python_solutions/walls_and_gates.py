from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        ROWS = len(rooms)
        COLS = len(rooms[0])

        def dfs(r, c, distance):
            if (0 <= r < ROWS and 
            0 <= c < COLS):
                if rooms[r][c] == -1 or (rooms[r][c] == 0 and distance > 0) or rooms[r][c] < distance:
                    return
                if distance <= rooms[r][c]:
                    rooms[r][c] = distance
                    dfs(r-1, c, distance + 1)
                    dfs(r+1, c, distance + 1)
                    dfs(r, c-1, distance + 1)
                    dfs(r, c+1, distance + 1)
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    dfs(r, c, 0)
        return rooms

solution = Solution()
print(solution.walls_and_gates([[0,-1],[2147483647,2147483647]]))