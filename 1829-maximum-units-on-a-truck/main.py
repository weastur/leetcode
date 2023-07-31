from operator import itemgetter

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=itemgetter(1), reverse=True)
        ans = 0
        idx = 0
        while truckSize and idx < len(boxTypes):
            cnt = min(truckSize, boxTypes[idx][0])
            ans += cnt * boxTypes[idx][1]
            truckSize -= cnt
            idx += 1
        return ans
        