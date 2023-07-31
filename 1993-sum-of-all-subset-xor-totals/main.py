import itertools

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for l in range(1, len(nums) + 1):
            for c in itertools.combinations(nums, l):
                cur = 0
                for x in c:
                    cur ^= x
                ans += cur
        return ans 