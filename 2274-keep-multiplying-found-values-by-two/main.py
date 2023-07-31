class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while True:
            try:
                nums.index(original)
            except ValueError:
                return original
            else:
                original *= 2