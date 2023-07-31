class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = sum(x % 2 for x in position)
        even = sum(1 - x % 2 for x in position)
        return min(odd, even)
        