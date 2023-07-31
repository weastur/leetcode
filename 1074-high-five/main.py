from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for item in items:
            scores[item[0]].append(item[1])
        for values in scores.values():
            values.sort(reverse=True)
        result = []
        for _id in scores:
            result.append([_id, sum(scores[_id][:5]) // 5])
        result.sort()
        return result
        