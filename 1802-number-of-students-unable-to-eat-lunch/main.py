class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches_f = sandwiches.count(0)
        students_f = students.count(0)
        if sandwiches_f == students_f:
            return 0
        elif sandwiches_f > students_f:
            val = 0
            d = sandwiches_f - students_f
        else:
            val = 1
            d = (len(sandwiches) - sandwiches_f) - (len(students) - students_f)
        for i in range(len(sandwiches) - 1, -1, -1):
            if sandwiches[i] == val:
                d -= 1
            if not d:
                return len(students) - i