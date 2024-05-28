a = [1,2,3,4,5]
d = 4
for i in range(d):
    end = a[0]
    a.pop(0)
    a.insert(len(a), end)
print(a)
