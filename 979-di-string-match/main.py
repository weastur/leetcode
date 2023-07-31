class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s) + 1
        l = -1
        r = n
        perm = []
        for ch in s:
            if ch == 'I':
                l += 1
                perm.append(l)
            else:
                r -= 1
                perm.append(r)
        perm.append(l + 1)
        return perm
        