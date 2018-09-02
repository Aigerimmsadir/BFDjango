import statistics
from decimal import Decimal
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(round(Decimal(statistics.mean(student_marks[query_name])),2))