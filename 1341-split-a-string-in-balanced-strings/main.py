class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        for ch in s:
            l += ch == 'L'
            r += ch == 'R'
            ans += l == r    
        return ans