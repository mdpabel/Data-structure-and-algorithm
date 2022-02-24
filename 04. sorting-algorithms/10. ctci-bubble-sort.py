#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

"""
3 2 1

i = 0
2 3 1
2 1 3

2

i = 1
1 2 3
3
1 2 3
3 -> break

i = 2
1 2 3
1 2 3

"""

def countSwaps(a):
    n = len(a)

    no_of_swap = 0
    for i in range(n):
        prev_swap = no_of_swap
        for j in range(n-1):
            if(a[j] > a[j + 1]):
                a[j],a[j+1] = a[j+1],a[j]
                no_of_swap += 1
                if(prev_swap == no_of_swap):
                    break
        if(prev_swap == no_of_swap):
            break
    print(f"Array is sorted in {no_of_swap} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
