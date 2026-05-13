def hash_set(listy, target):
    limited_set =  set(x for x in listy if x<target)
    for i in limited_set:
        difference = target - i
        if difference in limited_set:
            return [difference, i]
    return []

def h_s(listy, target):
    filtered_set = set(x for x in listy if x < target)
    for i in filtered_set:
        companion = target - i
        if companion in filtered_set:
            return [companion, i]
    return []
print(h_s([4,2, 7, 8, 3, 11, 15], 9))