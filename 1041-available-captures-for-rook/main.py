class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ans = 0
        x, y = 0, 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x, y = i, j
                    break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            a, b = x, y
            while a >= 0 and a < 8 and b >= 0 and b < 8:
                if board[a][b] in ['R', '.']:
                    a += dx
                    b += dy
                    continue
                elif board[a][b] == 'B':
                    break
                elif board[a][b] == 'p':
                    ans += 1
                    break
        return ans