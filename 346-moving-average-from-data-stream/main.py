class MovingAverage:

    def __init__(self, size: int):
        self._size = size
        self._arr = []
        

    def next(self, val: int) -> float:
        self._arr.append(val)
        n = min(len(self._arr), self._size)
        return sum(self._arr[-1 * n:]) / n


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)