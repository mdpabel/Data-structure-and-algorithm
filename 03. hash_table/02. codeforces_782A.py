"""
3
2 1 1 3 2 3

map = {
    2 : 2
    1 : 2
    3 : 1
}

count = 1

2 in map ? no
1 in map ? no
1 in map ? yes
3 in map ? no
2 in map ? yes


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

n = inp()
li = inlt()

map = {}

_max = 0

count = 0

for i in li:
    if i in map:
        count -= 1
    else:
        count += 1
    map[i] = True
    _max = max(_max, count)

print(_max)