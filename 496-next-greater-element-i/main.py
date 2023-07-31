class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        for j in range(len(nums1)):
            idx = -1
            for i in range(len(nums2)):
                if nums2[i] == nums1[j]:
                    idx = i
                elif idx != -1 and nums2[i] > nums1[j]:
                    ans[j] = nums2[i]
                    break
        return ans