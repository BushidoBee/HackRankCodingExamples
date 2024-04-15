from collections import namedtuple
cases = int(input())
Student = namedtuple('Student', input().split())
marks_sum = 0

for i in range(cases):
    learner = input().split()
    marks_sum += int(Student(*learner).MARKS)
print("%.2f" % (marks_sum / cases))
