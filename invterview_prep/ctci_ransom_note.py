def checkMagazine(magazine, note):
    magazine_dict = {}
    for word in magazine:
        if word in magazine_dict:
            magazine_dict[word] += 1
        else:
            magazine_dict[word] = 1

    for word in note:
        if word in magazine_dict and magazine_dict[word] > 0:
            magazine_dict[word] -= 1
        else:
            print('No')
            return

    print('Yes')