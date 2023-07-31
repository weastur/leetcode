class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        ans = 0
        for ch in stones:
            ans += ch in j
        return ans