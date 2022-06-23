import sys
from turtle import right
input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))


# 🔥🔥🔥
n, q = inlt()

prefix_sum = []

h = 0
g = 0
j = 0

prefix_sum.append([h, g, j])

for _ in range(n):
    item = inp()
    if item == 1:
        h += 1
    if item == 2:
        g += 1
    if item == 3:
        j += 1
    prefix_sum.append([h, g, j])


for _ in range(q):
    a, b = inlt()
    left = prefix_sum[a-1]
    right = prefix_sum[b]
    res = [right[0]-left[0], right[1]-left[1], right[2]-left[2]]
    print(res)


""" 
2,1,1,3,2,1

[0,0,0]
[0,1,0]
[1,1,0]
[2,1,0]
[2,1,1]
[2,2,1]
[3,2,1]



"""
