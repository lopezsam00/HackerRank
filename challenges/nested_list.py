student_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
flatten = [x for sublist in student_list for x in sublist if isinstance(x, float)]
flatten = list(set(flatten))
flatten.sort()
second_lowest = flatten[1]
dumm = []
for i in student_list:
    if i[1] == second_lowest:
        dumm.append(i[0])
dumm.sort()
for i in dumm:
    print(i)    