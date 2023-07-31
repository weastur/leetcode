class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if nums[j] - nums[i] < diff:
                    continue
                if nums[j] - nums[i] > diff:
                    break
                for k in range(j, n):
                    if nums[k] - nums[j] < diff:
                        continue
                    if nums[k] - nums[j] > diff:
                        break
                    ans += 1
        return ans
        