s1 = 'Hello'
s2 = 'World'

def twoStrings(s1, s2):
    for i in s2:
        if s1.__contains__(i):
            return 'YES'
    for i in s1:
        if s2.__contains__(i):
            return 'YES'
    return 'NO'

print(twoStrings(s1, s2))