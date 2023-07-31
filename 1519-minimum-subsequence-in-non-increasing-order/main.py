class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        nums.sort(reverse=True)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            total -= nums[i]
            if s > total:
                return nums[:i + 1]
        