from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        c = Counter(nums)
        for x in c:
            if c[x] != 1:
                return x