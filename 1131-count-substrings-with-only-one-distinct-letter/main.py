class Solution:
    def countLetters(self, s: str) -> int:
        ans = 0
        cur = 1
        s += 'X'
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                ans += (cur * (cur + 1)) // 2
                cur = 1
            else:
                cur += 1
        return ans