from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        return max((x for x in c if c[x] == 1), default=-1)