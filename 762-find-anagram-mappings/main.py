class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        used = [False] * n
        ans = [0] * n
        for i in range(n):
            for j in range(n):
                if not used[j] and nums2[j] == nums1[i]:
                    used[j] = True
                    ans[i] = j
                    break
        return ans