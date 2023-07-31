class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        num = 0
        for ch in s:
            ans += ch == '*' and num % 2 == 0
            num += ch == '|'
        return ans 
        