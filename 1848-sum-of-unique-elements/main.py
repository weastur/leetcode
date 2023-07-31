from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = 0
        for x in c:
            ans += x if c[x] == 1 else 0
        return ans