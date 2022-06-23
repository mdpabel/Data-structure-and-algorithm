"""
3 10
8 12 20
1 1 1

10
8 11

"""
import sys
import math
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

#
t = inp()


for i in range(t):
    n,k = inlt()
    a = inlt()
    b = inlt()

    map = {}

    for i in range(n):
        str = a[i],i
        map[str] = b[i]

    sorted_map = sorted(map)

    for item in sorted_map:
        if item[0] <= k:
            k += map[item]

    print(k)