class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = []
        for i in range(n - 2):
            max_local.append([0] * (n - 2))
        for i in range(n - 2):
            for j in range(n - 2):
                max_local[i][j] = max(max(grid[i][j:j+3]), max(grid[i+1][j:j+3]), max(grid[i+2][j:j+3]))
        return max_local