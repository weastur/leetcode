class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(s <= queryTime <= f for s, f in zip(startTime, endTime))
        