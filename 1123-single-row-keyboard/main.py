class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = [0] * 26
        for i in range(26):
            pos[ord(keyboard[i]) - ord('a')] = i
        ans = pos[ord(word[0]) - ord('a')]
        for i in range(1, len(word)):
            ans += abs(pos[ord(word[i]) - ord('a')] - pos[ord(word[i - 1]) - ord('a')])
        return ans