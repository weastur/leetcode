from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s = set(arr2)
        c = Counter(x for x in arr1 if x in s)
        c2 = Counter(x for x in arr1 if x not in s)
        ret = []
        for x in arr2:
            for _ in range(c[x]):
                ret.append(x)
        ending = list(c2.elements())
        ending.sort()
        return ret + ending
        