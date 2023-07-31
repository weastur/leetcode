class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        mmin = min(nums)
        return 1 if mmin > 0 else 1 - mmin