class Solution:
    def replaceDigits(self, s: str) -> str:
        ret = list(s)
        for i in range(1, len(s), 2):
            ret[i - 1] = s[i - 1]
            ret[i] = chr(ord(ret[i - 1]) + int(s[i]))
        return ''.join(ret)