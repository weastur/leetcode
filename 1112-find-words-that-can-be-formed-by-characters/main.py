from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        c = Counter(chars)
        for word in words:
            wc = Counter(word)
            for ch in wc:
                if wc[ch] > c[ch]:
                    break
            else:
                ans += len(word)
        return ans 