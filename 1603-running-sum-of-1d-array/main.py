class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = [nums[0]]
        for num in nums[1:]:
            sums.append(sums[-1] + num)
        return sums