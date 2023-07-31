class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        f, s = s.split(':')
        ret = []
        for col in range(ord(f[0]), ord(s[0]) + 1):
            for row in range(int(f[1]), int(s[1]) + 1):
                ret.append(chr(col) + str(row))
        return ret