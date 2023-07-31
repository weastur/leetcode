class Solution:
    def freqAlphabets(self, s: str) -> str:
        pos = len(s) - 1
        ret = []
        while pos >= 0:
            if s[pos] != '#':
                ret.append(chr(ord('a') + int(s[pos]) - 1))
                pos -= 1
            else:
                ret.append(chr(ord('a') + int(s[pos - 2]) * 10 + int(s[pos - 1]) - 1))
                pos -= 3
        return ''.join(ret[::-1])              
        