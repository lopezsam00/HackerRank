n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print('{:0.2f}'.format(sum(student_marks[query_name])/3))

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika