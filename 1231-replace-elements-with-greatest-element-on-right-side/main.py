class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mmax = [0] * n
        mmax[n - 1] = -1
        for i in range(n - 2, -1, -1):
            mmax[i] = max(mmax[i + 1], arr[i + 1])
        return mmax