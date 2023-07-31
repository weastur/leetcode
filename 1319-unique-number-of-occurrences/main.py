from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        counts = set(c.values())
        return len(c) == len(counts)