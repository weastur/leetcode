class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        n = len(mat)
        j = n - 1
        for i in range(n):
            s += mat[i][i] + mat[i][j]
            j -= 1
        if n % 2 == 1:
            s -= mat[n // 2][n // 2]
        return s
        