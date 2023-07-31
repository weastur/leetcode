class OrderedStream:

    def __init__(self, n: int):
        self._n = n
        self._ptr = -1
        self._arr = [''] * self._n
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self._arr[idKey - 1] = value
        last = self._ptr
        while self._ptr + 1 < self._n and self._arr[self._ptr + 1] != '':
            self._ptr += 1
        ans = self._arr[last + 1:self._ptr + 1] if self._ptr != last else []
        return ans
        
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)