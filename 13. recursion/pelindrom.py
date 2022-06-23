def isPelindrom(str):
    n = len(str)
    if n == 0 or n == 1:
        return True

    if str[0] == str[-1]:
        return isPelindrom(str[1: n-1])

    return False


print(isPelindrom('racecar'))
