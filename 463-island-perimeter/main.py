class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i == 0 or grid[i - 1][j] == 0:
                    ans += grid[i][j]
                if i == m - 1 or grid[i + 1][j] == 0:
                    ans += grid[i][j]
                if j == 0 or grid[i][j - 1] == 0:
                    ans += grid[i][j]
                if j == n - 1 or grid[i][j + 1] == 0:
                    ans += grid[i][j]
        return ans
        