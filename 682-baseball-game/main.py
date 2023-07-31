class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for op in operations:
            n = len(rec)
            if op == '+':
                rec.append(rec[n - 1] + rec[n - 2])
            elif op == 'D':
                rec.append(rec[n - 1] * 2)
            elif op == 'C':
                rec.pop()
            else:
                rec.append(int(op))
        return sum(rec)