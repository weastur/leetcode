class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        s = 0
        for ch in str(min(nums)):
            s += ord(ch) - ord('0')
        return 1 - s % 2