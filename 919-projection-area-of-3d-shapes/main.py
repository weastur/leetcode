class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                ans += grid[i][j] != 0
        for i in range(n):
            ans += max(grid[i])
        for j in range(n):
            mmax = 0
            for i in range(n):
                mmax = max(mmax, grid[i][j])
            ans += mmax
        return ans