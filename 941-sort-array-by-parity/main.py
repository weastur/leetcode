class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = []
        r = []
        for x in nums:
            if x % 2 == 0:
                l.append(x)
            else:
                r.append(x)
        return l + r