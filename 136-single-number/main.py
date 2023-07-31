from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for val in c:
            if c[val] == 1:
                return val