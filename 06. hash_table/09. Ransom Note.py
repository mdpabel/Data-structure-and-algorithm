def checkMagazine(magazine, note):
    # Write your code here
    map = defaultdict(int)

    for word in magazine:
        map[word] += 1

    isTrue = True
    for word in note:
        if not map[word] > 0:
            print("No")
            isTrue = False
            break
        else:
            map[word] -= 1

    if isTrue:
        print("Yes")
