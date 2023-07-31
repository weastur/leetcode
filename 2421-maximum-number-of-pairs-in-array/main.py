from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = [0, 0]
        for x in set(nums):
            ans[0] += c[x] // 2
            ans[1] += c[x] % 2
        return ans
        