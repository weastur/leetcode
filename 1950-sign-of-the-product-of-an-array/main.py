class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        for x in nums:
            if not x:
                return 0
            neg += x < 0
        if neg % 2 == 1:
            return -1
        return 1