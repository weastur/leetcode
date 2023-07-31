class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        for i in range(1, numRows):
            curr = [0] * (i + 1)
            for j in range(i + 1):
                if j == 0 or j == i:
                    curr[j] = 1
                else:
                    curr[j] = ret[-1][j - 1] + ret[-1][j]
            ret.append(curr)
        return ret