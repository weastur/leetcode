class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strlen = len(strs[0])
        n = len(strs)
        ans = 0
        for j in range(strlen):
            for i in range(1, n):
                if strs[i - 1][j] > strs[i][j]:
                    ans += 1
                    break
        return ans