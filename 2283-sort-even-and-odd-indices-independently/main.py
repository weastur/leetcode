class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odds = nums[1::2]
        evens = nums[::2]
        odds.sort(reverse=True)
        evens.sort()
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = evens[i // 2]
            else:
                nums[i] = odds[i // 2]
        return nums