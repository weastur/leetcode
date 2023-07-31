class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0] if n % 2 == 1 else []
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-1 * i)
        return res
        