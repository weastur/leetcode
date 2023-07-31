class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ret = [[x, y] for x in range(rows) for y in range(cols)]
        ret.sort(key=lambda point: abs(point[0] - rCenter) + abs(point[1] - cCenter))
        return ret