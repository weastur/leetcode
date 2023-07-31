from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        return sum(c[i] * (c[i] - 1) // 2 for i in c)
        