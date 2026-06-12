# Write a function that finds all pairs in a list that sum to a target value

def find_pairs(nums, target):
    seen = set()
    used = set()
    found = []
    for i in nums:
        diff = target - i
        smaller = min(diff, i)
        bigger = max(diff, i)
        if diff in seen and (smaller, bigger) not in used:
            pair = (smaller, bigger)
            found.append(pair)
            used.add(pair)
        seen.add(i)

    return found

print(find_pairs([2, 7, 4, 3, 1, 6], target=8))


