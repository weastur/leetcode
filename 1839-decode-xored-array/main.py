class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for value in encoded:
            arr.append(arr[-1] ^ value)
        return arr
        