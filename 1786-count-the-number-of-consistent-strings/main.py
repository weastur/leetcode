class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        a = set(allowed)
        for word in words:
            ans += set(word).issubset(a)
        return ans
        