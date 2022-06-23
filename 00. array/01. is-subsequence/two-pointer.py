def isSubsequence(s: str, t: str) -> bool:
    p1 = 0
    p2 = 0

    n = len(s)
    m = len(t)

    while p1 < n and p2 < m:
        if s[p1] == t[p2]:
            p1 += 1
            p2 += 1
        else:
            p2 += 1
    return p1 == n
