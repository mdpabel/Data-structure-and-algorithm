"""
1   2   3   4   2   1
1 < 2
    2 < 3
        3 < 4
            4 < 2 ? false
                4 > 2
                    2 > 1


"""
def isValid(li):
    n = len(li)

    if(n < 3):
        return False

    i = 1

    while i < n and li[i] > li[i-1]:
        i += 1

    if i == 1 or i == n:
        return False

    while i < n and li[i] < li[i-1]:
        i += 1

    if(i == n):
        return True
    else:
        return False

print(isValid([3,5,5]))
print(isValid([0,3,2,1]))
print(isValid([1,3,2]))