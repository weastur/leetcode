from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        ret = []
        for el, cnt in Counter(nums).most_common():
            for _ in range(cnt):
                ret.append(el)
        ret.reverse()
        return ret