def longest_substr(stringy):
    longest = ""
    left = 0
    seen = {}

    for right, chary in enumerate(stringy):
        if chary in seen and seen[chary] >= left:
            left = right +1
        seen[chary] = right

        if right - left +1 > len(longest):
            longest = stringy[left:right+1]
    return longest

x = longest_substr("aabbbadea")
print(x)
