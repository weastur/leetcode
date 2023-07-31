class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        nums = [(str(bin(x)).count('1'), x) for x in arr]
        nums.sort()
        return [x[1] for x in nums]
        