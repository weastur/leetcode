class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = [(row.count(1), i) for i, row in enumerate(mat)]
        arr.sort()
        ret = [row[1] for row in arr[:k]]
        return ret