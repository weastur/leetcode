class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = int(nums[0] != 0)
        for i in range(1, len(nums)):
            ans += nums[i] != nums[i - 1]
        return ans