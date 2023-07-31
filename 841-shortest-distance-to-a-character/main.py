class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        d = [0] * n
        nxt = prev = -1
        for i in range(n):
            if nxt < i or nxt == -1:
                if nxt != -1:
                    prev = nxt
                nxt = s.find(c, i)
            if prev == -1:
                d[i] = abs(i - nxt)
            else:
                d[i] = min(abs(i - nxt), abs(i - prev))
        return d