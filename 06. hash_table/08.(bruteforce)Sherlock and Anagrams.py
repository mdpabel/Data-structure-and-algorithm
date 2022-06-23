#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

"""
abba

a b b a
ab bb ba
abb bba

a a
b b
ab ba
abb bba

cdcd
c d c d
cd dc cd
cdc dcd

c c
d d
cd cd

kkkk

k k k k
kk kk kk
kkk kkk



"""

def sherlockAndAnagrams(s):
    # Write your code here
    n = len(s)
    list = []
    for i in range(n):
        for j in range(n-i):
            sorted_item = ''.join(sorted(s[j:j+i+1]))
            list.append(sorted_item)

    count = 0
    list_len = len(list)

    for i in range(list_len):
        for j in range(i + 1, list_len):
            if list[i] == list[j]:
                count += 1
            if len(list[i]) < len(list[j]):
                break
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
