from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        w = defaultdict(lambda: 0)
        for item in items1 + items2:
            w[item[0]] += item[1]
        ret = []
        for k, v in w.items():
            ret.append([k, v])
        ret.sort()
        return ret