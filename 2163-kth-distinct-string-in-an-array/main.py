from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        for word in arr:
            if c[word] == 1:
                k -= 1
            if not k:
                return word
        return ''