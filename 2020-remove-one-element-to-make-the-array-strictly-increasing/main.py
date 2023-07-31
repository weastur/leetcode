class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                continue
            cnt += 1
            if i - 1 == 0 or nums[i - 2] < nums[i]:
                continue
            if i + 1 == len(nums) or nums[i - 1] < nums[i + 1]:
                continue
            return False
        return cnt <= 1