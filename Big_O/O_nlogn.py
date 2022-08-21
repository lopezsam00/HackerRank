def nlogn(n):
    y = n//2
    while y > 1:
        for i in range(n):
            print(i)
        y = y//2

nlogn(4)
