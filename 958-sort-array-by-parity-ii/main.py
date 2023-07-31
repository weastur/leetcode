class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        n = len(nums)
        while True:
            while i < n and nums[i] % 2 == 0:
                i += 2
            while j < n and nums[j] % 2 == 1:
                j += 2
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        return nums