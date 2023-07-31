class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        plus = sum(map(lambda op: 1 if op.find('+') != -1 else 0, operations))
        return plus * 2 - len(operations)
        