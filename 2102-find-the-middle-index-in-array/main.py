class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = nums[:]
        right = nums[:]
        n = len(nums)
        for i in range(1, n):
            left[i] = left[i] + left[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i] + right[i + 1]
        for i in range(n):
            ls = left[i - 1] if i > 0 else 0
            rs = right[i + 1] if i < n - 1 else 0
            if ls == rs:
                return i
        return -1
        