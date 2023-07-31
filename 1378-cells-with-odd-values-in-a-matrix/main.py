from collections import Counter

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = Counter(x[0] for x in indices)
        cols = Counter(x[1] for x in indices)
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += (rows[i] + cols[j]) % 2
        return ans
        