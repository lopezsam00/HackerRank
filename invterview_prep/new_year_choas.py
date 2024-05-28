def minimum_bribes(q):
    new = [x -1 -q.index(x) if x-1-q.index(x) > 0 else 0 for x in q]
    check_two = [xx if xx <= 2 else -1000000 for xx in new]
    print(sum(check_two) if sum(check_two) > 0 else "Too chaotic")
