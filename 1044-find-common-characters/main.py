from string import ascii_lowercase
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = [Counter(word) for word in words]
        ret = []
        for ch in ascii_lowercase:
            cur = min(c[ch] for c in cnt)
            if cur:
                ret.extend([ch] * cur)
        return ret