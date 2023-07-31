class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights[:]
        expected.sort()
        return sum(a != b for a, b in zip(expected, heights))
        