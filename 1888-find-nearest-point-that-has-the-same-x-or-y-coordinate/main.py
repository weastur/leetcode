class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mmin = min(filter(lambda point: point[0] == x or point[1] == y, points), key=lambda point: abs(point[0] - x) + abs(point[1] - y), default=-1)
        try:
            return points.index(mmin)
        except ValueError:
            return -1