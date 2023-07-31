class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(abs(max(nums) - min(nums)) - 2 * k, 0)