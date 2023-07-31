class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            cur = 0
            for num2 in nums:
                cur += num2 < num
            ans.append(cur)
        return ans
        