class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ret = []
        mmin = 999999999
        for i in range(len(arr) - 1):
            mmin = min(mmin, arr[i + 1] - arr[i])
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == mmin:
                ret.append([arr[i - 1], arr[i]])
        return ret