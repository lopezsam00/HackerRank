def most_frequent(listy):
    counts = {}
    for i, num in enumerate(listy):
        if not num in counts:
            counts[num] = {"count": 0, "first_seen":i}
        counts[num]["count"] +=1
    return max(counts, key=lambda x: (counts[x]["count"], -counts[x]["first_seen"]))

def mas_frequente(listy):
    count = {}
    for i, num in enumerate(listy):
        if num not in count:
            count[num] = {"count":0, "first_seen":i}
        count[num]["count"] +=1
    return max(count, key=lambda x: (count[x]["count"], -count[x]["first_seen"]))
    

print(mas_frequente([1, 3, 3, 2, 1, 1,4,4,4,5]))