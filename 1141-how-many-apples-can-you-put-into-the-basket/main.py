class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        ans = 0
        cur = 5000
        idx = 0
        while idx < len(weight) and cur - weight[idx] >= 0:
            cur -= weight[idx]
            idx += 1
            ans += 1
        return ans