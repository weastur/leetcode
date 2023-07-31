class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        rows = [min(row) for row in matrix]
        cols = matrix[0][:]
        for i in range(1, m):
            for j in range(n):
                cols[j] = max(cols[j], matrix[i][j])
        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == rows[i] and matrix[i][j] == cols[j]:
                    ans.append(matrix[i][j])
        return ans