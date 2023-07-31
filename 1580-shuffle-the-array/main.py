class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l, r, i = 0, n, 0
        ans = [0] * 2 * n
        while r < 2 * n:
            ans[i] = nums[l]
            ans[i + 1] = nums[r]
            l += 1
            r += 1
            i += 2
        return ans
        