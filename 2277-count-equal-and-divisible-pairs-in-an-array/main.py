class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (i * j) % k != 0:
                    continue
                ans += nums[i] == nums[j]
        return ans