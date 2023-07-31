class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        sums = arr
        for i in range(1, n):
            sums[i] = sums[i - 1] + sums[i]
        for i in range(0, n):
            for j in range(i, -1, -2):
                left = sums[j - 1] if j > 0 else 0
                ans += sums[i] - left
        return ans