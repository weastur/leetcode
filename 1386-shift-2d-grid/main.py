from itertools import chain

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        long = list(chain.from_iterable(grid))
        k %= len(long)
        if not k:
            return grid
        ans = []
        cur = len(long) - k
        for _ in range(len(grid)):
            row = []
            for _ in range(len(grid[0])):
                row.append(long[cur])
                cur = (cur + 1) % len(long)
            ans.append(row)
        return ans