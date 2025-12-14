class Solution(object):
    def countStudents(self, students, sandwiches):

        from collections import Counter
        count = Counter(students)
        for s in sandwiches:
            if count[s] == 0:
                break
            count[s] -= 1
        return sum(count.values())
