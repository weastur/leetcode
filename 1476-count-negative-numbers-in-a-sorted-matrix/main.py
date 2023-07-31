class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            for num in row:
                ans += num < 0
        return ans