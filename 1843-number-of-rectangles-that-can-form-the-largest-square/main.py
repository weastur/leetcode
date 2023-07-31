class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = [min(x[0], x[1]) for x in rectangles]
        return max_len.count(max(max_len))