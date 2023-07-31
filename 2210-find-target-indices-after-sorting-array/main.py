class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        try:
            start = nums.index(target)
        except ValueError:
            start = -1
        while -1 < start < len(nums) and nums[start] == target:
            ans.append(start)
            start += 1
        return ans